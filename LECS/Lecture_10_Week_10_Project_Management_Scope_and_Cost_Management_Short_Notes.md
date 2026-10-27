# Lecture 10 — Week 10: Project Management — Scope and Cost Management

## Scope concepts

- **Product scope:** features and functions of the product/service/result.
- **Project scope:** work required to deliver the product with those features.
- **Scope creep:** uncontrolled expansion without approved changes to time, cost, resources, or risk.

## Scope management processes

1. **Plan scope management:** decide how scope and requirements will be defined, validated, and controlled.
2. **Collect requirements:** use interviews, workshops, observation, surveys, prototypes, and document analysis.
3. **Define scope:** create a detailed project/product description, deliverables, acceptance criteria, assumptions, and exclusions.
4. **Create WBS:** decompose deliverables into manageable work packages.
5. **Validate scope:** obtain formal customer/sponsor acceptance of completed deliverables.
6. **Control scope:** monitor status and process changes through integrated change control.

The **scope baseline** consists of the approved scope statement, WBS, and WBS dictionary. Requirements traceability connects each requirement to its source, deliverable, test, and status.

### Requirement types and collection

- **Business requirements:** organizational goal/value, e.g., improve online service.
- **Stakeholder/user requirements:** what a stakeholder needs to accomplish.
- **Functional requirements:** behavior/capability, e.g., users can transfer funds.
- **Non-functional requirements:** quality/constraint, e.g., response within two seconds.
- **Technical/transition requirements:** platform, integration, migration, training, or deployment constraints.
- Collection tools: interviews, brainstorming, facilitated workshops, focus groups, surveys, observation, document analysis, prototypes, benchmarking, and decision techniques.

The **Requirements Traceability Matrix (RTM)** links requirement ID and source to business objective, priority, owner, design/build component, acceptance criterion, test case, delivery/version, and status. It helps prevent omission and unauthorized addition.

### Scope process revision table

| Process | Main techniques | Key outputs |
|---|---|---|
| Plan scope management | Expert judgment, analysis, meetings | Scope management plan; requirements management plan |
| Collect requirements | Interviews, workshops, surveys, observation, prototypes | Requirements documentation; RTM |
| Define scope | Product/alternatives analysis, facilitation, expert judgment | Project scope statement; document updates |
| Create WBS | Decomposition, expert judgment | WBS, WBS dictionary, scope baseline |
| Validate scope | Inspection/demo, decision making, meetings | Accepted deliverables, change requests, performance information |
| Control scope | Variance/data analysis, change-control system | Performance information, change requests, baseline/document updates |

The scope statement should include objectives, deliverables, in-scope work, exclusions, assumptions, constraints, and acceptance criteria. The **100% rule** says the WBS covers 100% of approved project work without extra work. A **work package** is the lowest level practical for estimating, ownership, scheduling, and control.

**Validate scope vs control quality:** quality control checks technical correctness/defects and produces verified deliverables; scope validation obtains formal stakeholder/customer acceptance. They support each other but are not interchangeable.

### Predictive and Agile scope

- Predictive projects establish a detailed baseline and use formal integrated change control.
- Agile maintains a prioritized product backlog, expresses needs as user stories with acceptance criteria, selects work during sprint planning, delivers increments, and adapts from reviews/feedback.
- Agile welcomes valuable change but does not permit uncontrolled work: Product Owner priority, backlog transparency, capacity, Definition of Done, and acceptance criteria provide control.

## Cost management processes

1. Plan cost management.
2. Estimate costs.
3. Determine the budget by aggregating estimates and reserves into a time-phased cost baseline.
4. Control costs by monitoring actuals, forecasts, and approved changes.

Estimation methods include analogous, parametric, bottom-up, three-point, expert judgment, and vendor bid analysis. Contingency reserve addresses identified uncertainty within the baseline; management reserve covers unknown/management-controlled uncertainty outside it.

### Cost process revision table

| Process | Purpose | Key output |
|---|---|---|
| Plan cost management | Define units, accuracy, thresholds, reporting, funding, and control rules | Cost management plan |
| Estimate costs | Approximate labor, hardware, software/licenses, cloud, training, vendors, facilities, reserves | Activity cost estimates and basis of estimates |
| Determine budget | Aggregate estimates by work package/time; add contingency; reconcile funding limits | Time-phased cost baseline and funding requirements |
| Control costs | Compare actual/earned performance, forecast, manage changes and corrective action | Cost performance/forecasts and change/update records |

Estimation comparison:

- **Analogous:** quick top-down comparison with a similar project; cheapest, normally least precise.
- **Parametric:** unit rate × quantity using a reliable statistical relationship.
- **Bottom-up:** estimate detailed activities/work packages and aggregate; slower but often more accurate.
- **Three-point:** optimistic `O`, most likely `M`, pessimistic `P`; triangular `(O + M + P)/3` or PERT `(O + 4M + P)/6`.
- **Vendor bid/expert judgment:** useful when specialist market knowledge is needed; assumptions must be documented.

## Earned Value Management (EVM)

- **PV:** planned value of scheduled work.
- **EV:** budgeted value of completed work.
- **AC:** actual cost of completed work.
- **CV = EV − AC:** negative means over budget.
- **SV = EV − PV:** negative means behind schedule.
- **CPI = EV / AC:** below 1 indicates poor cost efficiency.
- **SPI = EV / PV:** below 1 indicates poor schedule efficiency.
- A common forecast is **EAC = BAC / CPI** when current cost performance is expected to continue.

Additional revision formulas:

- `VAC = BAC − EAC`: expected budget variance at completion.
- `ETC = EAC − AC`: expected additional cost from now.
- `TCPI = (BAC − EV) / (BAC − AC)` to meet original BAC, or `(BAC − EV) / (EAC − AC)` to meet approved EAC.
- Forecast choice must match assumptions; do not mechanically use `BAC/CPI` if future work is expected to behave differently.

Interpretation table:

| Metric | Favorable | Unfavorable |
|---|---|---|
| CV | `> 0` under budget | `< 0` over budget |
| SV | `> 0` ahead | `< 0` behind |
| CPI | `> 1` cost efficient | `< 1` cost inefficient |
| SPI | `> 1` ahead | `< 1` behind |

## Change control

Document the request, analyze impact across all constraints, obtain the proper approval/rejection, update plans/baselines, communicate the decision, and verify implementation. Never hide required change merely to preserve an outdated baseline.

## Exam reminders

- Validate scope is customer acceptance; control quality checks correctness.
- A WBS is deliverable-oriented decomposition, not merely a calendar.
- Learn EVM formulas and interpret signs/ratios, not only calculate them.
- In IT scenarios, explicitly trace an added feature through scope, estimate, budget, schedule, resource, quality, and risk impacts before approval.
