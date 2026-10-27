# Lecture 11 — Week 11: Procurement, Resource, and Schedule Management

## Procurement management

Procurement obtains products or services from outside the project organization.

1. **Plan procurement:** make-or-buy analysis, requirements/SOW, contract type, criteria, risks, and procurement strategy.
2. **Conduct procurement:** invite bids/proposals, answer questions fairly, evaluate sellers, negotiate, and award.
3. **Control procurement:** monitor performance, changes, claims, payment, compliance, acceptance, and closure.

Common contract types:

- **Fixed-price:** more cost risk on seller; works best with clear scope.
- **Cost-reimbursable:** buyer pays allowable costs plus fee; useful with uncertain scope but exposes buyer to more cost risk.
- **Time and materials:** pays agreed labor/material rates; flexible but needs caps and monitoring.

Evaluation should consider capability, quality, security, legal compliance, support, total cost, financial stability, and delivery—not price alone.

### Procurement process detail

- **Plan:** make-or-buy analysis, market research, procurement SOW/specification, contract type, source-selection criteria, roles, schedule, budget, risk, legal/security/data clauses.
- **Conduct:** bidder conference/RFI/RFQ/RFP, advertising/shortlisting, proposal evaluation, independent estimates, negotiation, seller selection, agreement award.
- **Control:** inspect service/deliverables, compare SLA/KPI and contract, manage relationships/changes/claims, verify invoices, audit compliance, accept/close, and document lessons.
- A **procurement SOW** specifies deliverable/service, scope, technical/quality standards, dates, acceptance, reporting, location, data/security, and responsibilities clearly enough for comparable proposals.

Contract risk allocation:

| Contract | Cost uncertainty mainly borne by | Suitable situation |
|---|---|---|
| Firm fixed price | Seller | Well-defined stable scope |
| Fixed price with incentive/adjustment | Mostly seller, with agreed mechanisms | Clear base scope plus performance/economic uncertainty |
| Cost reimbursable | Buyer | Uncertain/innovative work where scope cannot be defined sufficiently |
| Time and materials | Buyer unless capped | Staff augmentation or short flexible work with controlled rates |

Make-or-buy considers strategic importance, internal capability/capacity, total lifecycle cost, schedule, confidentiality/IP, quality, supplier market, scalability, and dependency/lock-in.

## Resource management

Resources include people, equipment, facilities, materials, and infrastructure.

- Plan resource management and define roles/responsibilities.
- Estimate resource needs for activities.
- Acquire resources and negotiate availability.
- Develop the team through skills, trust, feedback, and team norms.
- Manage performance, motivation, conflict, and change.
- Control physical resources and address shortages or waste.

A **RACI** chart identifies who is Responsible, Accountable, Consulted, and Informed. Each activity should have clear accountability. Resource calendars show availability; histograms show demand. **Resource leveling** may change the critical path/end date, while **resource smoothing** works within available float where possible.

### Resource processes and tools

1. **Plan resource management:** team charter, roles, responsibility/authority/competency, organization chart, acquisition/release, training, recognition, physical-resource control.
2. **Estimate activity resources:** determine type/quantity of people, equipment, material, and facilities using bottom-up/analogous/parametric estimates and alternatives analysis.
3. **Acquire resources:** negotiate internal people and procure/hire external resources; confirm assignments and calendars.
4. **Develop team:** training, team building, ground rules, co-location/virtual collaboration, recognition, and assessment.
5. **Manage team:** observe performance, coach, give feedback, resolve conflict, and manage changes.
6. **Control resources:** ensure physical resources are available and used as planned; correct shortage, waste, loss, or variance.

Conflict responses can include collaborate/problem solve, compromise/reconcile, smooth/accommodate, force/direct, and withdraw/avoid. Choose based on stakes, urgency, relationship, and ability to reach a durable solution.

## Schedule management

1. Plan schedule management.
2. Define activities from work packages.
3. Sequence activities using dependencies.
4. Estimate durations using evidence and uncertainty.
5. Develop and baseline the schedule.
6. Control progress and approved changes.

Dependency relationships are finish-to-start, start-to-start, finish-to-finish, and start-to-finish. Leads accelerate a successor; lags introduce waiting time.

### Dependency and estimation revision

- **Mandatory/hard logic:** physically or legally required.
- **Discretionary/soft logic:** preferred sequence based on practice.
- **External:** controlled outside project, such as regulator/vendor approval.
- **Internal:** controlled within project.
- Duration estimates: analogous, parametric, bottom-up, and three-point. PERT expected duration is `E = (O + 4M + P) / 6`.
- Milestones have zero duration and mark approvals, releases, or significant events.

## Critical Path Method

The critical path is the longest-duration path through the network and determines the earliest finish. Activities on it normally have zero total float. Delay on a critical activity delays the project unless corrective action changes the network or duration.

Schedule compression:

- **Crashing:** add resources/cost to shorten duration where feasible.
- **Fast tracking:** overlap activities previously done sequentially; increases risk/rework potential.

CPM calculation reminders:

- Forward pass: `EF = ES + duration`; successor ES is the largest predecessor EF.
- Backward pass: `LS = LF − duration`; predecessor LF is the smallest successor LS.
- `Total float = LS − ES = LF − EF` (depending on counting convention used in the question).
- Near-critical paths with little float also need monitoring. Resource limits can alter the practical critical path.

### Schedule control and EVM

Track actual start/finish, remaining duration, milestone trends, dependencies, resource availability, and approved changes against the schedule baseline. Analyze variance/root cause, forecast completion, and use corrective/preventive action.

- `SV = EV − PV`; positive ahead, negative behind.
- `SPI = EV / PV`; above 1 ahead, below 1 behind.
- `CV = EV − AC`; positive under budget, negative over budget.
- `CPI = EV / AC`; above 1 cost efficient, below 1 over budget.
- Lecture example `PV=100,000`, `EV=90,000`, `AC=110,000`: `SV=-10,000`, `SPI=0.90`, `CV=-20,000`, `CPI≈0.82`; behind schedule and over budget.

## Exam reminders

- Match contract type to scope certainty and risk allocation.
- Distinguish resource leveling from smoothing.
- Critical means schedule-driving, not necessarily most expensive or technically difficult.
- Link the three areas: late procurement delays resource availability; resource shortage changes durations; schedule compression can increase cost, quality, procurement, and risk exposure.
