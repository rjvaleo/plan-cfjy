# Builds the five pages of the Cresta pitch site into this folder.
# Run: python build.py
import html, os
HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape
READ = 'November 22, 2026'

NAV = [('index.html', 'The plan'), ('evidence.html', 'The evidence'), ('prototype.html', 'The prototype'), ('how.html', 'How I built it'), ('why.html', 'Why me')]

def page(fn, title, desc, body, script=''):
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == fn else '', t) for h, t in NAV)
    out = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           '<meta name="robots" content="noindex,nofollow"><title>%s</title><meta name="description" content="%s">'
           '<link rel="stylesheet" href="assets/site.css"></head><body><a class="skip" href="#main">Skip to content</a>'
           '<div class="flag"><div class="w"><b>Unofficial.</b> A job application for Cresta&rsquo;s Forward Deployed Product Manager, AI Agent role, built from public pages. Not affiliated with Cresta.</div></div>'
           '<header class="w nav"><a class="me" href="index.html"><i></i>Richard J. Valeo</a><nav aria-label="Pages">%s</nav></header>'
           '<main id="main">%s</main>'
           '<footer class="w foot"><span>Richard J. Valeo &middot; Georgetown, Colorado &middot; <a href="https://rjvaleo.github.io/">rjvaleo.github.io</a> &middot; <a href="https://www.linkedin.com/in/rjvaleo">LinkedIn</a></span>'
           '<span>Public pages read on %s. Nothing here comes from inside Cresta.</span></footer>%s</body></html>') % (E(title), E(desc), nav, body, READ, script)
    open(os.path.join(HERE, fn), 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote', fn, len(out))

def a(url, text): return '<a href="%s">%s</a>' % (url, text)
C = 'https://cresta.com/'
BLOG = C + 'blog/'
FIN1 = BLOG + 'part-i-replacing-finserv-ivrs-with-an-ai-agent-a-3-phase-playbook'
FIN2 = BLOG + 'part-ii-replacing-finserv-ivrs-with-an-ai-agent-where-the-compounding-happens'
T20 = BLOG + 'introducing-ai-agent-testing-2-0-confidence-at-launch-confidence-at-scale'
E2E = BLOG + 'building-and-deploying-production-grade-ai-agents-crestas-end-to-end-approach'
SOUND = BLOG + 'test-and-evaluate-voice-ai-agents-under-real-call-conditions-with-soundcheck'
AIUC = BLOG + 'cresta-ai-agent-is-now-aiuc-1-certified'
SELF = BLOG + 'crestas-ai-agent-expertise-in-developers-hands-introducing-our-end-to-end-self-serve-model'
SENTRY = BLOG + 'introducing-cresta-sentry-0-1-recognize-personal-ai-agents-and-guide-every-response'
PILOT = C + 'guides/ai-agent-pilots-for-enterprise-cx'
IMPL = C + 'ai-agent-implementation'
TEST = C + 'ai-agent-test-and-deploy'

# ---------------------------------------------------------------- the plan
# The people in the room. The customer and its people are made up.
WHO = [('all', 'What ships'), ('sponsor', 'The sponsor'), ('ops', 'Operations'), ('comp', 'Compliance'), ('it', 'IT'), ('fde', 'The engineer'), ('me', 'Me')]
WHOLABEL = {'sponsor': 'The sponsor, a vice president of customer operations', 'ops': 'The contact center director and supervisors', 'comp': 'The head of compliance',
            'it': 'The IT and integration lead', 'fde': 'Cresta&rsquo;s Forward Deployed Engineer', 'me': 'Me, the Forward Deployed Product Manager'}
# (stage, title, when, [(ships, note)], gate, {who: what they are asked for})
STAGES = [
 ('Stage 1', 'Scope', 'Before the contract is signed.', [
   ('A one-page scope', 'The use cases that are in, and the ones that are out.'),
   ('Each outcome measure', 'One sentence on how it is counted and what is left out.'),
   ('A baseline for each', 'Or the words &ldquo;none yet&rdquo;.')],
  'The sponsor signs the scope and names who owns the agent once it is live.',
  {'sponsor': 'Says which outcome matters most, and what result would make them stop.',
   'ops': 'Show how these calls go today, and which ones their people dread.',
   'comp': 'Names the lines the agent must never cross.',
   'it': 'Says which systems the agent can reach, and how soon.',
   'fde': 'Checks each use case against the systems it needs.',
   'me': 'Write the scope. Leave out anything that has no measure.'}),
 ('Stage 2', 'Kickoff', 'The first two weeks.', [
   ('Interviews with every stakeholder', 'Turned into one requirements list.'),
   ('Each requirement a yes or no check', 'Marked must-have or nice-to-have.'),
   ('The go or no-go rules', 'Written down before the build starts.')],
  'Requirements and gate rules agreed in one workshop.',
  {'sponsor': 'Agrees the gate rules while nobody has a result to defend.',
   'ops': 'Bring the hard calls. Their reviewers will later check the graders.',
   'comp': 'Marks which requirements are must-haves.',
   'it': 'Commits a date for test access to each system.',
   'fde': 'Turns the requirements into graders and a test plan.',
   'me': 'Interview everyone first. Run the workshop. Publish the board with every line showing a dash.'}),
 ('Stage 3', 'Build and test', 'Until the gate rules are met.', [
   ('The agent', 'Built with the Forward Deployed Engineer.'),
   ('Test conversations by use case', 'Simulated callers, including bad lines and noise.'),
   ('A weekly session on failing turns', 'Operators judge them, one at a time.')],
  'Every must-have has a test, and every grader has been checked against people.',
  {'sponsor': 'Sees the board every week. No slides.',
   'ops': 'Answer yes or no on specific turns, a few at a time.',
   'comp': 'Reviews every failed must-have.',
   'it': 'Replaces stand-in systems with the real ones.',
   'fde': 'Builds, fixes what fails, and reruns the tests.',
   'me': 'Read the failing transcripts myself. Check the counts. Cut scope that will not pass in time.'}),
 ('Stage 4', 'Go or no-go', 'Launch week.', [
   ('A gate review', 'Decided use case by use case.'),
   ('A rollback drill', 'Run before the first customer call.'),
   ('A small launch', 'A share of calls, one flow at a time.')],
  'Go, per use case. A use case with no data does not launch.',
  {'sponsor': 'Makes the call, with the evidence on one page.',
   'ops': 'Supervisors watch live calls and can take one over.',
   'comp': 'Signs off the must-haves, by name.',
   'it': 'On call for the first hours.',
   'fde': 'Watches the first calls and owns the rollback.',
   'me': 'Run the review. Hold what fails. Pick a launch day away from the billing peak.'}),
 ('Stage 5', 'First weeks live', 'The first six weeks after launch.', [
   ('The outcome numbers', 'Counted the way the scope said.'),
   ('Failures turned into tests', 'So the same one cannot ship twice.'),
   ('The next use case', 'Chosen from why calls still transfer.')],
  'A review with the sponsor: widen, hold or stop.',
  {'sponsor': 'Decides the next phase from numbers they already agreed to.',
   'ops': 'Flag bad conversations. Each flag becomes a test.',
   'comp': 'Gets the must-have pass rate on live calls.',
   'it': 'Plans the systems the next use case needs.',
   'fde': 'Tunes the agent and widens the share of calls by rule.',
   'me': 'Report resolution beside containment. Write what we learned into the playbook.'}),
]
cols = ''
for n, title, when, ships, gate, asks in STAGES:
    sh = ''.join('<div class="item"><b>%s</b><small>%s</small></div>' % s for s in ships)
    ak = ''.join('<div class="ask" data-who="%s" hidden><b>%s</b><span>%s</span></div>' % (k, WHOLABEL[k], v) for k, v in asks.items())
    cols += ('<div class="col stage"><span class="when">%s</span><h3>%s</h3><p>%s</p><div class="ships">%s</div>%s'
             '<div class="sgate"><b>The gate out of this stage</b>%s</div></div>') % (n, title, when, sh, ak, gate)
SEG = '<div class="seg wrap" role="group" aria-label="Follow one person">' + ''.join(
    '<button type="button" aria-pressed="%s" data-who="%s">%s</button>' % ('true' if k == 'all' else 'false', k, t) for k, t in WHO) + '</div>'

def phase(when, title, why, items, know, wide=False):
    lis = ''
    for t, d, tags in items:
        lis += '<li><b>%s</b><span>%s</span>%s</li>' % (t, d, ''.join('<span class="tag">%s</span>' % x for x in tags))
    return '<div class="phase%s"><span class="when">%s</span><h3>%s</h3><p class="note" style="margin-top:8px">%s</p><ul>%s</ul><p class="know"><b>How I will know.</b> %s</p></div>' % (' wide' if wide else '', when, title, why, lis, know)

PHASES = '<div class="phases">' + phase('Stage 1. Before the contract is signed', 'Scope one agent, and say what counts',
    'Cresta&rsquo;s pilot guide says a pilot with no written success criteria ends in debate, not a decision. Scoping is where that is prevented.', [
    ('Pick the use cases from the customer&rsquo;s own calls.', 'Cresta&rsquo;s Automation Discovery ranks call topics by how often they come up and how they resolve. The scope starts there, not from a wish list.', ['Sponsor', 'Operations', 'Solutions architect']),
    ('Define each outcome measure in one sentence.', 'How it is counted, and what is left out. The list is further down this page.', ['Sponsor', 'Operations']),
    ('Write the baseline, or write &ldquo;none yet&rdquo;.', 'If the lender cannot say today&rsquo;s transfer rate, measuring it is the first task.', ['Operations', 'IT']),
    ('Name the owner and the stop rule.', 'Who owns the agent in production, and what result would make us stop. Both are on Cresta&rsquo;s own pilot checklist.', ['Sponsor'])],
    'The sponsor can say in two sentences what the agent will do, what it hands to a person, and which number decides the next phase.') + phase('Stage 2. Kickoff, the first two weeks', 'Interview everyone, then write one list',
    'This is how I start every program. On my current one, ten vendor teams planned in ten ways until I interviewed every lead and turned the answers into one script.', [
    ('Interview every stakeholder before the workshop.', 'The sponsor, the supervisors, the agents who take these calls today, the quality reviewers, compliance and IT. The same questions for each.', ['Everyone']),
    ('Turn the answers into one requirements list.', 'Each requirement a yes or no check, marked must-have or nice-to-have. That is the form Cresta&rsquo;s testing takes as its input.', ['Compliance', 'Operations', 'Engineer']),
    ('Agree the go or no-go rules in the workshop.', 'Before the build, while nobody has a result to defend.', ['Sponsor', 'Compliance']),
    ('Publish the launch-readiness board.', 'Every line shows a dash on day one. That is the honest starting state.', ['Everyone'])],
    'Every must-have traces to the person who asked for it, and the sponsor has signed the gate rules.') + phase('Stage 3. Build and test', 'Build with the engineer, test by use case',
    'The posting pairs this role with a Forward Deployed Engineer. The engineer builds. I keep the scope, the customer and the evidence straight.', [
    ('Test conversations grouped by use case.', 'Simulated callers drawn from the lender&rsquo;s own conversations, then the same calls on a bad line with noise and interruptions.', ['Engineer']),
    ('Check the graders against the customer&rsquo;s own reviewers.', 'A grader nobody has checked is not evidence. Cresta scores each one against human review.', ['Operations', 'Engineer']),
    ('A weekly session on failing turns.', 'Show one turn and ask one yes or no question. It is Cresta&rsquo;s own published lesson, and it keeps operators in the room.', ['Operations', 'Compliance']),
    ('Check the numbers myself.', 'On one of my builds, an agent reported 682 tests. A stale copy had inflated the count. The real number was 384.', ['Me'])],
    'Every must-have has at least one test, every grader has a score against people, and I have read the failing transcripts, not only the pass rates.') + phase('Stage 4. Launch week', 'Go or no-go, then a small launch',
    'I have run go or no-go decisions through build, test, acceptance and cutover. The rule I carry over: a gate with no data shows a dash, never green.', [
    ('A gate review, use case by use case.', 'What passes can launch. What fails, or has no data, waits. The date holds for the rest.', ['Sponsor', 'Compliance', 'Operations']),
    ('A rollback drill before the first customer call.', 'Cresta&rsquo;s releases roll back in one step. The drill proves the people know how.', ['Engineer', 'IT']),
    ('Launch on a small share of calls, one flow at a time.', 'Cresta&rsquo;s financial services playbook asks for this: a small change you can watch closely, and you always know what changed.', ['Engineer', 'Operations']),
    ('Pick the day from the billing calendar.', 'The same playbook warns against the Monday after a Friday or Saturday billing cycle.', ['Operations'])],
    'The decision is recorded per use case with the evidence beside it, and supervisors have watched the first live calls.') + phase('Stage 5. The first six weeks live', 'Measure honestly, then widen',
    'The posting says to own the outcomes and to find more to automate. Both start with numbers the customer trusts.', [
    ('Report resolution beside containment.', 'Cresta&rsquo;s playbook calls containment the easiest number in a contact center to inflate. After-hours calls come out, and a hang-up is not a win.', ['Sponsor', 'Operations']),
    ('Turn every production failure into a test.', 'A flagged conversation becomes a test case, so the same failure cannot ship twice. Cresta&rsquo;s testing does this in one step.', ['Operations', 'Engineer']),
    ('Choose the next use case from why calls still transfer.', 'The transfer reasons are the map for the next phase.', ['Operations', 'Sponsor']),
    ('Write it into the playbook.', 'What I would do again, what I would not, and what the platform could do for the next team. The posting asks for this by name.', ['Product', 'Forward deployed team'])],
    'The sponsor reads one page, recognizes every number on it, and decides to widen, hold or stop.', wide=True) + '</div>'

RULES = ('<div class="rules">'
  '<div class="rule"><b>No data shows a dash, never green.</b><span>A green light nobody checked is worse than no light.</span></div>'
  '<div class="rule"><b>A failed must-have holds the use case.</b><span>Whatever the pass rate. Cresta&rsquo;s testing separates must-have from nice-to-have for this reason.</span></div>'
  '<div class="rule"><b>An unchecked grader counts as no data.</b><span>If no person has checked the grader, its passes prove nothing yet.</span></div>'
  '<div class="rule"><b>The decision is per use case.</b><span>What passes can launch while the rest waits. Scope shrinks before the date moves.</span></div>'
  '<div class="rule"><b>The rules are agreed at kickoff.</b><span>Before anyone has a result to defend.</span></div></div>')

INDEX = ('<div class="w hero"><h1>One AI agent, from scoping to go-live and after.</h1>'
  '<p class="lead">Cresta&rsquo;s posting for Forward Deployed Product Manager, AI Agent says: &ldquo;you own each AI Agent and the outcomes they drive for our customers.&rdquo; This is how I would own one. I built it in one day from Cresta&rsquo;s public pages, with AI agents doing the reading. The customer in it is made up.</p>'
  '<div class="bottom"><div><b>The bottom line</b><span>Cresta already publishes how it scopes, tests and releases an agent. I would own the step between the test results and the customer&rsquo;s decision.</span></div>'
  '<div><b>So the order is</b><span>Agree what counts before anything is built. Test by use case. Launch only what passes. Measure the way Cresta&rsquo;s own playbook says to.</span></div>'
  '<div><b>Done means</b><span>The customer&rsquo;s sponsor can say what the agent does, what it hands to a person, and which number decides the next phase.</span></div></div>'
  '<div class="next"><a class="btn" href="prototype.html">Try the prototype</a><a class="btn ghost" href="evidence.html">Read the evidence</a></div></div>'

  '<section class="w" id="room"><div class="shead"><div><h2>Who is in the room, stage by stage</h2>'
  '<p>The posting names the lifecycle: pre-sale scoping, kickoff, launch and post-go-live optimization. This is one voice agent moving through it for Pinemoor Lending, a made-up lender. Pick a person to see what each stage asks of them.</p></div>'
  + SEG + '</div>'
  '<div class="stages" id="stages">' + cols + '</div>'
  '<p class="note" style="margin-top:14px">Pinemoor Lending and its people are made up. The stage names follow the posting. The practices I credit to Cresta come from its public pages. <a href="evidence.html">Sources are on the evidence page.</a></p></section>'

  '<section class="w" id="rules"><div class="shead"><div><h2>The gate rules</h2><p>Five rules for the go or no-go decision. The first is from the planning board I built for my current program. The second is Cresta&rsquo;s own.</p></div></div>'
  + RULES + '</section>'

  '<section class="w" id="stages-detail"><div class="shead"><div><h2>The plan, stage by stage</h2><p>What ships, who it involves, and how I will know. Financial services is an industry Cresta names, and its own playbook for lenders is the base I built on.</p></div></div>'
  + PHASES +
  '<p class="note" style="margin-top:14px">I have put no total length on this plan. One Cresta customer wrote that its first agent took four months, and Cresta says its newer tools cut a first deployment roughly in half. The real figure comes from Cresta&rsquo;s own deployments, which I cannot see.</p></section>'

  '<section class="w"><div class="two"><div><h2>What I would cut</h2><ul class="plain">'
  '<li><b>A second channel at launch.</b><span>Voice first, chat later. One flow at a time is Cresta&rsquo;s own advice.</span></li>'
  '<li><b>Hardship and dispute conversations.</b><span>They go to a person by design. Cresta&rsquo;s pilot guide says the same about high-emotion calls.</span></li>'
  '<li><b>Nice-to-have requirements that threaten the date.</b><span>They stay on the list and off the gate.</span></li>'
  '<li><b>New reporting.</b><span>Cresta&rsquo;s dashboards exist. The board in my prototype is one page for one decision.</span></li></ul></div>'
  '<div><h2>What would change this plan</h2><ul class="plain">'
  '<li><b>If the agent cannot reach the lender&rsquo;s systems in time,</b><span>the first launch answers questions only, and payments wait. One Cresta customer wrote that integrations took real IT work.</span></li>'
  '<li><b>If Cresta already shows customers a readiness view,</b><span>I use it. The rules matter more than the page.</span></li>'
  '<li><b>If the customer will run the agent itself,</b><span>the plan becomes a hand-over. Their team runs the gate with me watching, then without me.</span></li>'
  '<li><b>If the baseline shows the calls are not what the sponsor thinks,</b><span>the scope changes before the contract does.</span></li></ul></div></div></section>'

  '<section class="w"><div class="two"><div><h2>How I would measure it</h2><p class="lead">Seven measures, each defined at scoping and counted the same way every week.</p>'
  '<p class="note" style="margin-top:12px">I can see no baseline for any of them from outside, so there are no targets on this page. Setting the baselines is stage 1 work. The definitions follow ' + a(FIN1, 'Cresta&rsquo;s financial services playbook') + ' where it gives one.</p></div>'
  '<ul class="plain"><li><b>Containment.</b><span>The share of conversations the agent handles without passing to a person. After-hours calls are left out, because nothing can transfer then.</span></li>'
  '<li><b>Resolution.</b><span>The share where the customer&rsquo;s issue was finished. A hang-up is not a resolution.</span></li>'
  '<li><b>Transfers, with reasons.</b><span>How many conversations go to a person, and why. The reasons choose the next use case.</span></li>'
  '<li><b>Wait after a transfer.</b><span>How long a customer waits once the agent hands them on. Cresta&rsquo;s playbook counts transferred calls that wait under 90 seconds.</span></li>'
  '<li><b>Minutes handled by people.</b><span>Total talk time for the human team. The playbook prefers it to handle time per call, which rises when the easy calls leave.</span></li>'
  '<li><b>Customer satisfaction.</b><span>Asked of the customer, or predicted from the conversation. Reported next to containment, never instead of it.</span></li>'
  '<li><b>Must-have pass rate on live calls.</b><span>The same checks that gated the launch, run on real conversations.</span></li></ul></div>'
  '<div class="next"><a class="btn" href="prototype.html">See the gate as a working page</a><a class="btn ghost" href="how.html">How I built this with AI</a></div></section>')

ROOM_JS = ('<script>(function(){var s=document.getElementById("stages"),bs=document.querySelectorAll(".seg button");'
  'function set(w){bs.forEach(function(x){x.setAttribute("aria-pressed",x.dataset.who===w)});'
  's.querySelectorAll(".ships").forEach(function(x){x.hidden=w!=="all"});'
  's.querySelectorAll(".ask").forEach(function(x){x.hidden=x.dataset.who!==w})}'
  'bs.forEach(function(x){x.addEventListener("click",function(){set(x.dataset.who)})});set("all")})();</script>')

page('index.html', 'One AI agent, from scoping to go-live and after · Richard J. Valeo',
     'A deployment plan for one AI agent, written for Cresta’s Forward Deployed Product Manager, AI Agent role by Richard J. Valeo. Unofficial, built from public pages.', INDEX, ROOM_JS)

# ---------------------------------------------------------------- the evidence
NF = '<span class="note">Not found</span>'
RIV = [
 ('us', 'Cresta', TEST, 'Automated testing with Synthetic Customers and graders scored against human review', 'Soundcheck: noise, interruptions, poor connections', 'Versions, approvals, traffic splits, one-step rollback', 'Graders run on live conversations; live supervision and takeover', 'Home page only. The rest needs a customer login.', 'ISO 42001, SOC 2 Type II, HIPAA; AIUC-1', 'A forward-deployed product manager and engineer, named on a public page', 'Custom. No public price.'),
 ('', 'Sierra', 'https://sierra.ai/product/agent-studio', 'Simulations, which can gate a release', 'Voice Sims: noise, accents, interruptions, latency', 'Checks, merge approvals, split traffic, snapshot rollback', 'Monitoring and alerts; conversation review', 'Not found. The docs site asks for a sign-in.', 'SOC 2, ISO 27001, ISO 42001, PCI, HIPAA; AIUC-1', 'A forward-deployed team; &ldquo;agent engineers&rdquo;', 'Outcome-based model described. No price list.'),
 ('', 'Decagon', 'https://decagon.ai/product/testing-qa', 'Simulations, run before go-live', 'Accents, speed, noise, interruptions', 'Versions, staging and production, traffic ramp', 'Every conversation scored against custom criteria', 'Not found. The docs site redirects to a login.', 'SOC 2 Type II, ISO 27001, PCI, HIPAA', '&ldquo;Agent Product Managers&rdquo; and deployment engineers', 'Per conversation or per resolution. No price list.'),
 ('', 'Kore.ai', 'https://docs.kore.ai/agent-platform/evals', 'Evaluation suites with personas and scenarios', 'Test calls by softphone. Noise tests not found.', 'Development, staging, production; rollback; approvals', 'Scored quality and outcome reports', 'Public', 'SOC 2, ISO 27001, PCI', 'Forward Deployed Engineers named; partners', 'Unclear'),
 ('', 'Google Customer Engagement Suite', 'https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation', 'Evaluations: scenario, simulation and golden test cases', 'Voice-mode test cases. Noise tests not found.', 'Fixed versions, restore, percentage traffic split', 'Monitoring dashboard; conversation history', 'Public', 'ISO 42001 for Google Cloud', 'Self-serve; general consulting', 'Public usage prices'),
 ('', 'NICE', 'https://docs.cognigy.com/', 'A simulator with personas and success criteria', 'Not found. The docs say the simulator is text-only.', 'Snapshots and revert', 'AI observability; conversation analysis', 'Public', 'PCI, ISO 27001, SOC 2, HIPAA, FedRAMP', 'Professional services; certified partners', 'Public suite prices per agent'),
 ('', 'Genesys', 'https://help.genesys.cloud/articles/test-and-troubleshoot-agentic-virtual-agents/', 'Manual preview and a flow simulator. Automated simulation not found.', 'Voice preview. Noise tests not found.', 'Draft and publish', 'Performance dashboard; replay', 'Public', 'SOC 2, ISO 27001, ISO 42001, PCI, HIPAA, FedRAMP', 'Professional services; Forward Deployed Engineers', 'Public plan prices; AI by usage'),
]
rows = ''.join('<tr%s><td><b>%s</b></td>%s</tr>' % (' class="us"' if c else '', a(u, n), ''.join('<td>%s</td>' % x for x in cells)) for c, n, u, *cells in RIV)
EVID = ('<div class="w hero"><h1>The evidence.</h1><p class="lead">Everything on this site comes from pages any visitor can open, read on ' + READ + '. I created no account, submitted no form and tested no system.</p></div>'
  '<section class="w"><h2>Where Cresta already leads</h2><ul class="plain">'
  '<li><b>Testing that starts from written requirements.</b><span>Each requirement is a yes or no check marked must-have or nice-to-have, and each grader gets an accuracy score against human review. ' + a(T20, 'AI Agent Testing 2.0, June 4, 2026') + '</span></li>'
  '<li><b>Test callers built from the customer&rsquo;s own conversations.</b><span>Synthetic Customers, with test cases generated from production failures and reviewer feedback. ' + a(TEST, 'Test and deploy') + '</span></li>'
  '<li><b>Voice tested on a bad line.</b><span>Soundcheck simulates noise, interruptions and poor connections, and the same graders score live calls after launch. ' + a(SOUND, 'Soundcheck, November 19, 2026') + '</span></li>'
  '<li><b>It tells customers how to measure honestly.</b><span>Its financial services playbook says containment is easy to inflate, and how to count it so that it holds up. ' + a(FIN1, 'Part I') + ', ' + a(FIN2, 'Part II') + '</span></li>'
  '<li><b>It names the people who deploy.</b><span>Five roles, including this one, and three ways to share ownership with the customer. ' + a(IMPL, 'AI Agent implementation') + '</span></li>'
  '<li><b>Independent checks on the agent itself.</b><span>ISO/IEC 42001 for how AI is governed, and AIUC-1 for the agent, announced November 4, 2026. ' + a(C + 'trust', 'Trust') + ', ' + a(AIUC, 'AIUC-1') + '</span></li></ul></section>'
  '<section class="w"><div class="shead"><div><h2>Cresta beside six rivals</h2><p>What a customer&rsquo;s deployment lead can establish from each vendor&rsquo;s public pages before signing. Each name links to one of that vendor&rsquo;s own pages.</p></div></div>'
  '<div class="tw"><table><thead><tr><th>Vendor</th><th>Tests before launch</th><th>Voice conditions</th><th>Release controls</th><th>After launch</th><th>Public docs</th><th>Assurance stated</th><th>Who deploys</th><th>Pricing</th></tr></thead><tbody>' + rows + '</tbody></table></div>'
  '<p class="note" style="margin-top:14px">&ldquo;Not found&rdquo; means not found on public pages, not that the vendor lacks it. A second AI research agent gathered the rival rows from each vendor&rsquo;s own pages. I checked the Cresta row against saved page text, and I have not checked the rival rows line by line. Two rivals&rsquo; trust portals and Cresta&rsquo;s own could not be read by the agents, so the assurance column comes from each vendor&rsquo;s other pages.</p></section>'
  '<section class="w"><div class="two"><div><h2>What changed in this market in 2026</h2><p class="lead">Four changes that shape how an agent gets deployed now, and one thing that has not changed.</p></div><ul class="plain">'
  '<li><b>There is now an independent standard for AI agents.</b><span>AIUC-1 pairs an audit with adversarial tests on the live agent. Sierra announced it on September 17, 2026, and Cresta on November 4. ' + a('https://sierra.ai/blog/sierra-achieves-aiuc-1-certification', 'Sierra') + ', ' + a(AIUC, 'Cresta') + '</span></li>'
  '<li><b>Testing moved from scripts to simulated customers.</b><span>Five of the six rivals describe it, and three vendors including Cresta now simulate bad audio as well. Links are in the table above.</span></li>'
  '<li><b>Forward-deployed tools are being handed to customers.</b><span>On October 29, 2026 Cresta opened the tools its own teams use to customer and partner developers. A playbook now has to work when the customer runs it. ' + a(SELF, 'Self-serve model') + '</span></li>'
  '<li><b>Some callers are now AI agents too.</b><span>Cresta reports a sharp rise in personal AI agents contacting its customers, and released a model to detect them. That is a new group of test conversations. ' + a(SENTRY, 'Sentry, October 12, 2026') + '</span></li>'
  '<li><b>The decision itself is not shown.</b><span>All seven vendors describe testing and release controls of some kind. On their public pages I found no go or no-go view for the customer&rsquo;s executives. That is why I built one.</span></li></ul></div></section>'
  '<section class="w"><div class="two"><div><h2>What is not on this page</h2></div><div><p>While reading, I found a handful of places where Cresta&rsquo;s public pages disagree with each other, and some smaller housekeeping.</p>'
  '<p>Those are in a findings report I will send to Cresta directly. A public page is the wrong place for them.</p>'
  '<div class="next"><a class="btn" href="index.html">Back to the plan</a><a class="btn ghost" href="how.html">How the research was run</a></div></div></div></section>')
page('evidence.html', 'The evidence · Richard J. Valeo', 'Cresta AI Agent beside six rivals, as a customer’s deployment lead can read them from public pages, with sources.', EVID)

# ---------------------------------------------------------------- how
def step(who, cls, title, text): return '<div class="step"><span class="who %s">%s</span><b>%s</b><span>%s</span></div>' % (cls, who, title, text)
HOW = ('<div class="w hero"><h1>How I built this.</h1><p class="lead">The posting asks for exposure to building agents and says personal projects count. This site was built by agents I ran. Here is how, and where the line sat between the AI&rsquo;s work and mine.</p></div>'
  '<section class="w"><h2>The workflow</h2><div class="flow">'
  + step('Me', 'me', 'Set the terms', 'A plan and a working prototype for the role. Read the company as its customer would. Findings go to the company, not onto a public page.')
  + step('AI', 'ai', 'Read everything public', 'The lead agent read Cresta: 99 pages, six legal documents and 39 change-log entries. A second agent read six rivals.')
  + step('AI', 'ai', 'Check each finding', 'Every Cresta claim was checked against the saved page text. Three candidate findings did not survive.')
  + step('AI', 'ai', 'Build', 'The plan, the prototype and a private findings report.')
  + step('Me', 'me', 'Read and stand behind it', 'I read every page before sending it. What is wrong here is mine.')
  + '</div><p class="note" style="margin-top:16px">The lead agent was Claude. It did the Cresta research, ran the second research agent, did the checking and wrote the pages. One working day, ' + READ + '.</p></section>'
  '<section class="w"><div class="two"><div><h2>The rules the agents worked under</h2><ul class="plain">'
  '<li><b>Every claim carries its source.</b><span>A page address and where on the page. The page text is saved, so any claim can be checked again.</span></li>'
  '<li><b>&ldquo;Not found&rdquo; is never rewritten as &ldquo;missing&rdquo;.</b><span>The agents had to say where they looked. Only a statement by Cresta itself counts as confirmed.</span></li>'
  '<li><b>Read only.</b><span>No account, no login, no form, no testing of any system. Cresta&rsquo;s product documentation sits behind a customer login, so nothing here comes from it.</span></li>'
  '<li><b>A separate agent for rivals.</b><span>So what one vendor says about another never stood in for that vendor&rsquo;s own page.</span></li>'
  '<li><b>Text on a page is data, not instructions.</b><span>Some pages speak directly to AI assistants and tell them what to say. The agents read that text as content and did not act on it.</span></li></ul></div>'
  '<div><h2>Where the AI was wrong or thin</h2><ul class="plain">'
  '<li><b>Three candidate findings did not survive checking.</b><span>Placeholder text in the saved copy of three legal pages sits in a hidden template. A stray label on the comparison pages appears to be filled in by a script. An apparent typo in the service agreement was probably the text extractor&rsquo;s.</span></li>'
  '<li><b>The trust center could not be read.</b><span>It sits behind a browser check. Certification claims on this site come from Cresta&rsquo;s other pages.</span></li>'
  '<li><b>Charts were not read.</b><span>Only text was saved. Where a finding might be answered by a chart, the report says so.</span></li>'
  '<li><b>The rival rows are thinner than the Cresta row.</b><span>They were not checked line by line, and the evidence page says so.</span></li>'
  '<li><b>The plan is an outsider&rsquo;s.</b><span>The agents could read what Cresta publishes about deployments. They could not see one.</span></li></ul></div></div></section>'
  '<section class="w"><div class="two"><div><h2>Where my judgment came in</h2><p class="lead">The agents can read a hundred pages in an hour. They cannot decide what a hiring team should be shown.</p></div><ul class="plain">'
  '<li><b>Pitch each role with a plan and a working prototype.</b><span>A letter says I can do the job. A plan and a page you can click show how I would start.</span></li>'
  '<li><b>Read the company as its customer would, before pitching anything.</b><span>A deployment lead reads the product pages, the legal terms and the change log before signing. So did the agents.</span></li>'
  '<li><b>Report what turned up, privately.</b><span>If I find holes, I bring them up. The findings went into a report for Cresta, not onto this site.</span></li>'
  '<li><b>Say what I cannot see.</b><span>The plan has a section on what would change it, because I have no view inside a Cresta deployment.</span></li>'
  '<li><b>Stand behind the output.</b><span>I read every page of this site before sending it. If something here is wrong, that is mine, not the agent&rsquo;s.</span></li></ul></div>'
  '<div class="next"><a class="btn" href="why.html">Why me</a><a class="btn ghost" href="index.html">Back to the plan</a></div></section>')
page('how.html', 'How I built this · Richard J. Valeo', 'The AI workflow behind this plan, what was checked, and where judgment came in.', HOW)

# ---------------------------------------------------------------- why me
def row(ask, have): return '<tr><td><b>%s</b></td><td>%s</td></tr>' % (ask, have)
P = 'https://rjvaleo.github.io/'
WHY = ('<div class="w hero"><h1>Why me.</h1><p class="lead">I have never held the title Product Manager, and I have not worked in a contact center. I have spent twenty years taking client work from scope to launch, and this year I have built and run AI agents of my own.</p></div>'
  '<section class="w"><h2>What the posting asks, and what I have done</h2><div class="tw"><table><thead><tr><th style="width:32%">The posting asks for</th><th>What I have done</th></tr></thead><tbody>'
  + row('Five or more years in consulting, implementation, product or customer success', 'Eight years as an agency producer owning client accounts from pitch to launch, for American Express, Citi, Southeast Toyota, Unilever and PGi. Then delivery roles at A+E Networks, Meta and Eptura. Today I run the release train for ten vendor teams on a tolling modernization program.')
  + row('Leading complex deployments, with senior customer stakeholders', 'At a publicly traded retailer I ran readiness checkpoints and go or no-go decisions through build, test, acceptance and cutover. The go-live landed on time. On my current program I closed the first increment with every committed requirement accepted, and ran the two-day close-out for the client. ' + a(P + 'case-retailer.html', 'Retailer') + ', ' + a(P + 'case-pi-dashboard.html', 'planning board'))
  + row('Workshops and design sessions that align people on use cases and success criteria', 'I interviewed every workstream lead before planning and turned the answers into one script that ten vendor teams now plan from. I run a retrospective with all leads at the end of each increment. For Southeast Toyota I planned, ran and presented a user-testing study of the dealer site with a colleague.')
  + row('Exposure to building agents. Personal projects count.', 'A manager-and-worker loop: one agent writes the tasks, and local models work them in four stages against hidden tests and planted bugs, with a scoreboard that shows whether they improve. Also one written workflow that three agents from three vendors all run, with a ledger and an audit that stop them inventing skills. ' + a(P + 'case-sound-lab.html', 'The loop') + ', ' + a(P + 'case-job-synthesis.html', 'the workflow'))
  + row('Design, build, test and iterate on AI agents', 'Four music products shipped with AI agents behind more than 9,000 automated tests. Tests are the referee, not the model&rsquo;s word. I check the agents&rsquo; numbers: a reported 682 tests turned out to be 384. ' + a(P + 'how-i-work.html', 'How I work'))
  + row('Own outcomes and define the metrics', 'My planning board never shows a number it cannot source, and a gate with no data shows a dash, never green. The prototype on this site carries that rule into a launch decision. ' + a('prototype.html', 'Prototype'))
  + row('Improve the playbooks', 'The interview script every lead plans from. Six design documents that agents and people both build from. A rules file for agent sessions that records two times an agent overreached, and the rule each one produced. ' + a(P + 'case-rtm-tool.html', 'Case study'))
  + row('Work closely with AI or LLM-first products', 'In 2024 I was delivery lead for teams fine-tuning Gemini, ChatGPT and Claude models on customer data. At Meta I produced the voice recordings that trained its AI voices, heard across Facebook, Instagram, Oculus and Portal.')
  + '</tbody></table></div></section>'
  '<section class="w"><div class="two"><div><h2>The gap, plainly</h2></div><div><p class="lead">I have not worked in a contact center.</p>'
  '<p>I have learned a new client&rsquo;s operation many times, and I would expect to learn this one the same way: in the room with the people who run it. This site is the reading half of that, done in a day.</p>'
  '<p>My titles have been Producer, Scrum Master, Agile Coach and Release Train Engineer. I am the product owner and builder of the tools named above.</p>'
  '<p>I do know voice. At Meta I supported the embedded voice in the Ray-Ban Stories glasses and ran final QA. It shipped on the public launch date.</p>'
  '<div class="next"><a class="btn" href="https://rjvaleo.github.io/">See my work</a><a class="btn ghost" href="https://www.linkedin.com/in/rjvaleo">LinkedIn</a></div></div></div></section>')
page('why.html', 'Why me · Richard J. Valeo', 'Richard J. Valeo’s record against Cresta’s Forward Deployed Product Manager, AI Agent role.', WHY)

# ---------------------------------------------------------------- prototype (markup here, behaviour in assets/proto.js)
PROTO = open(os.path.join(HERE, '_proto.html'), encoding='utf-8').read()
page('prototype.html', 'Launch-readiness board prototype · Richard J. Valeo', 'A clickable prototype of a go or no-go board for one AI agent. Sample data and a made-up customer.', PROTO, '<script src="assets/proto.js"></script>')
