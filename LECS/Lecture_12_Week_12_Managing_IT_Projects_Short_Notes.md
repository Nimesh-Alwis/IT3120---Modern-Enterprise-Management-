# Lecture 12 — Week 12: Managing IT Projects

## Integrated view

This lecture brings together the project lifecycle and management of stakeholders, communications, scope, cost, schedule, resources, and procurement, then adds risk, quality, integration, change, delivery approaches, and AI assistance.

Modern success is more than “on time, within budget, to scope.” An IT product can meet those constraints yet fail if users cannot complete tasks reliably, value is not realized, quality/security are weak, or stakeholders reject the change. Evaluate delivery, product outcomes, business value, adoption, and sustainability.

## Risk management

A **risk** is an uncertain event or condition that may have a positive or negative effect; an **issue** has already occurred.

1. Plan how risk will be managed.
2. Identify threats and opportunities; record cause, event, and impact.
3. Perform qualitative analysis using probability, impact, urgency, and other factors.
4. Use quantitative analysis where its value justifies the effort.
5. Plan owners, triggers, responses, contingency, and residual/secondary risks.
6. Implement responses and monitor throughout delivery.

Threat responses: avoid, mitigate, transfer, accept, escalate. Opportunity responses: exploit, enhance, share, accept, escalate.

### Risk tools and artifacts

- Identification: brainstorming, interviews, expert judgment, checklists, SWOT, root-cause analysis, lessons learned, assumption/constraint analysis, and careful AI-assisted prompts.
- **Risk statement:** because of *cause*, an uncertain *event* may occur, leading to *effect on objectives*.
- **Risk register:** ID/category, cause/event/effect, owner, probability, impact, score/priority, triggers, response, contingency, residual/secondary risk, status.
- Qualitative score commonly uses `probability × impact`, supplemented by urgency, proximity, manageability, and stakeholder tolerance.
- Quantitative tools can include expected monetary value (`probability × financial impact`), decision trees, sensitivity analysis, and simulation.
- **Risk owner** monitors and ensures response; **action owner** carries out a particular response.

IT categories in the lecture: unclear/changing requirements; new technology/API/legacy integration; cybersecurity/data leakage; key-person loss; development delay; vendor/cloud failure; poor adoption; and regulatory/technology change.

Response example for an untested database: avoid by choosing established technology; mitigate via prototype/performance tests; transfer defined responsibility to a specialist supplier; or accept with monitoring and contingency resources.

## Quality management

Quality means fitness for use and conformance to agreed requirements—not maximum features or expensive perfection.

- **Plan quality:** standards, metrics, acceptance criteria, and activities.
- **Manage quality:** improve and audit processes; build quality into work.
- **Control quality:** inspect/test deliverables and analyze results.
- Prevention is normally cheaper than correcting defects after release.

IT techniques include peer review, automated testing, CI/CD controls, security testing, definition of done, defect analysis, root-cause analysis, and continuous improvement.

### Quality dimensions and measurable criteria

Software quality can include functionality, reliability, usability, performance, security, availability, maintainability, compatibility, scalability, and accessibility. Priority depends on the system and stakeholder needs.

- Replace “system should be fast” with a measurable requirement such as “95% of authenticated balance requests complete within 2 seconds under the agreed concurrent-user load.”
- Useful metrics: escaped defects, defect density/severity, test pass/coverage, response-time percentile, throughput, availability, mean time to recovery, failed-transaction rate, vulnerability severity/remediation time, task-completion rate, and accessibility conformance.
- **Cost of quality:** prevention + appraisal + internal failure + external failure. More prevention is justified when it reduces expensive failure/rework.
- Distinguish **grade** (category/features) from **quality** (conformance/fitness). A basic product can be high quality.

Testing types from the lecture include unit, integration, system, regression, performance, security, usability, and User Acceptance Testing (UAT). Each targets different failure risks.

Agile quality is continuous through acceptance criteria, Definition of Done, peer review, automated testing, CI, frequent demos, and retrospectives. Example DoD: code complete; peer reviewed; unit/integration/security checks pass; documentation updated; acceptance criteria satisfied; Product Owner accepts.

## Integration and change management

Integration management coordinates all project areas so decisions optimize the whole project rather than one local target. It includes chartering, plan integration, directing work, managing knowledge, monitoring work, integrated change control, and closure.

For a change: log it, analyze impact/value/risk, review under governance, approve/reject/defer, update baselines/backlog and documentation, communicate, implement, and verify. Organizational change also requires stakeholder readiness, sponsorship, training, support, and reinforcement.

### Seven integration processes

1. **Develop Project Charter** — authorize the project and connect it to business need/value.
2. **Develop Project Management Plan** — integrate subsidiary plans and baselines.
3. **Direct and Manage Project Work** — coordinate execution and produce deliverables/data.
4. **Manage Project Knowledge** — use existing knowledge and capture new lessons.
5. **Monitor and Control Project Work** — integrate performance, forecasts, issues, and recommended action.
6. **Perform Integrated Change Control** — evaluate cross-project impact and govern changes.
7. **Close Project or Phase** — acceptance, transition, administrative/contract closure, knowledge capture.

Integration requires trade-offs across the whole system. A request for biometric login affects scope, schedule, cost/licensing, security/privacy risk, specialist resources, procurement/API dependency, testing/quality, operations, compliance, and user stakeholders. The question is not only “can developers build it?” but “is its value worth the full impact and risk?”

### Integrated change control

1. Record a clear request and rationale.
2. Check completeness and authority.
3. Analyze benefit, scope, schedule, cost, resource, quality, risk, procurement, compliance, operations, and stakeholder impacts.
4. Obtain Change Control Board/Product Owner or designated approval.
5. Record approve/reject/defer decision and reasoning.
6. Update baseline, backlog, requirements, plans, contracts, risk/registers, and forecasts as applicable.
7. Communicate, implement, test, validate, and close the change.

An unapproved request is not authorized project work. An approved change changes the appropriate baseline—it is no longer “scope creep.”

## Waterfall, Agile, and Hybrid

- **Waterfall/predictive:** sequential planning and control; best where requirements and technology are stable or formal stage gates are important.
- **Agile/adaptive:** short iterations, prioritized backlog, frequent working increments, feedback, empowered cross-functional teams, and adaptation.
- **Hybrid:** combines methods intentionally—for example, fixed governance milestones with iterative software delivery.

Choose according to requirement volatility, risk, compliance, customer availability, architecture, team capability, contracting, and cost of change. Agile does not mean no planning or documentation.

| Dimension | Predictive/Waterfall | Agile/adaptive | Hybrid |
|---|---|---|---|
| Requirements | Defined in detail early | Evolve through feedback | Stable core plus adaptive areas |
| Delivery | Larger phase-based release | Frequent working increments | Mix of gates and increments |
| Change | Formal change control against baseline | Backlog reprioritization within governance | Method depends on component/change |
| Customer role | Reviews at defined milestones | Frequent collaboration and acceptance | Planned governance plus iterative feedback |
| Best fit | Stable scope, dependency/regulatory need | High uncertainty and learning value | Mixed conditions or transition environments |
| Main risk | Late feedback, costly rework | Scope/architecture/governance drift if poorly practiced | Complexity/confusion if interfaces are unclear |

Hybrid must be designed deliberately: clarify which work uses which method, how dependencies and reporting connect, and who owns decisions.

## AI-assisted project management

AI can assist with drafting plans, summarizing meetings, classifying issues, analyzing schedules, suggesting risks, generating test cases, and reporting. Human professionals remain accountable for validation, decisions, stakeholder judgment, ethics, security, and compliance.

Controls include approved tools, minimal/sanitized inputs, access restrictions, source verification, bias/error checks, version records, human approval, and no confidential data in unauthorized services.

### Good AI workflow

1. Define the task and decision context.
2. Supply only authorized, relevant, minimized context.
3. Request structured output and explicit assumptions (e.g., risk register fields or measurable quality metrics).
4. Challenge vague claims, missing risks, bias, fabricated sources, and incorrect calculations.
5. Validate against project records, subject experts, policies, contracts, and current stakeholder decisions.
6. Edit, approve, record provenance where required, and monitor real outcomes.

Useful applications: draft WBS/risk categories, meeting summaries/action extraction, alternative analysis, scenario simulation, schedule-risk flags, quality metrics/test cases, stakeholder-tailored drafts, knowledge retrieval, and report preparation. AI cannot own a risk, approve a change, negotiate stakeholder commitment, determine truth from missing data, or bear accountability.

### Example prompt pattern

> Given this authorized project context, identify risks as cause–event–effect statements. Return category, probability rationale, impact on objectives, early warning trigger, proposed owner role, and two response options. State assumptions and do not invent project facts.

The project team must still review and decide.

## Exam reminders

- Separate risks from issues and quality assurance from quality control.
- Justify delivery approach from project conditions instead of treating one method as universally best.
- Treat AI output as an unverified input, never as an accountable decision-maker.
- In integrated case answers, discuss value/adoption first, then trace effects through risk, quality, integration/change, delivery approach, and responsible AI use.
