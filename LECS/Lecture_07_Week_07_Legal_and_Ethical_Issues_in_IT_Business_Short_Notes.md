# Lecture 07 — Week 07: Legal and Ethical Issues in IT Business

## Law and ethics

- **Law** sets enforceable minimum standards backed by institutions and penalties.
- **Ethics** asks what is right, fair, responsible, and professionally acceptable.
- An action may be legal but still unethical; responsible IT decisions should satisfy both.

## Intellectual property and software licensing

- **Copyright:** protects original expression such as software code, documentation, and media.
- **Patent:** may protect eligible inventions for a limited period, subject to jurisdiction.
- **Trademark:** protects identifiers such as names, logos, and signs.
- **Trade secret:** protects commercially valuable confidential information when reasonable secrecy measures exist.

Software licenses define permitted use, modification, copying, and distribution. Proprietary, permissive open-source, and copyleft licenses impose different duties. Teams must keep a component inventory, review license compatibility, retain notices, and satisfy source/distribution obligations.

### License categories in the lecture

| Category | Source/usage position |
|---|---|
| Proprietary | Owned and controlled by a vendor; use, modification, copying, and sharing are restricted by the agreement |
| Open source | Source is available, but GPL, MIT, Apache, and other licenses impose different conditions |
| Freeware | Free of charge to use, but usually proprietary and not necessarily open source |
| Shareware | Limited/trial use; payment generally unlocks continued or full functionality |

Open source can be commercial. “Free” does not mean public domain or obligation-free.

## Privacy and data protection

Core principles include lawful/fair processing, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, and accountability.

Good practice includes informed notices, valid consent where required, access control, encryption, retention schedules, incident response, vendor review, and privacy by design. Collecting data because it *might* become useful conflicts with minimization.

Privacy concerns a person's control and appropriate use of personal data; confidentiality is a duty not to disclose entrusted information; integrity keeps data accurate/unaltered; security provides controls protecting confidentiality, integrity, and availability.

## Cybersecurity and computer misuse

Unauthorized access, interception, alteration, malware, fraud, and service disruption can create civil, criminal, contractual, and reputational consequences. Organizations need preventive controls, monitoring, backups, response procedures, evidence preservation, and clear authorization for security testing.

**Access-right principle:** authorized users receive only the permissions needed for their work (least privilege), supported by strong passwords, MFA, role-based access, logging, review, and detection. Monitoring must itself remain proportionate and privacy-aware.

Harmful actions include malware distribution, deliberate data destruction, unauthorized system alteration, misuse/damage of resources, and service disruption.

## Contracts and online business

IT agreements should clarify scope, acceptance criteria, price, ownership/licensing, confidentiality, service levels, data responsibilities, warranties, limitation of liability, termination, and dispute resolution. Electronic communications and signatures can create binding obligations when legal requirements are met.

## Ethical decision framework

1. Identify facts, stakeholders, duties, and uncertainties.
2. Identify legal, contractual, professional, and organizational rules.
3. Generate alternatives.
4. assess rights, harm/benefit, fairness, transparency, and long-term effects.
5. Decide, document, communicate, and monitor consequences.

Common issues include algorithmic bias, dark patterns, employee monitoring, surveillance, deceptive UX, accessibility exclusion, irresponsible AI, and conflicts of interest.

### Trade secrets and AI

Trade secrets may include confidential source code, algorithms/methods, business strategies, customer information, research, and unreleased product design. Protection depends on practical secrecy measures such as access restrictions, NDAs, classification, and secure development practices.

AI concerns include biased/discriminatory data or outcomes, transparency/explainability, human accountability for critical decisions, employment impact, safety/security, and misuse. Human judgment must remain in consequential decisions.

## Real-world cases from the lecture

- **Cambridge Analytica/Facebook:** personal data used for political profiling without informed understanding—privacy, consent, transparency, and trust failures.
- **Uber 2016 breach:** millions of user/driver records accessed—security, breach disclosure, accountability, and data-protection issues.
- **Amazon recruiting AI:** historical data produced gender bias—fairness, discrimination, validation, and human oversight issues.
- **Pratibha Syntex:** alleged unlicensed Microsoft/Adobe use led to settlement and audits—copyright, license compliance, and respect for creators.

## Professional practice and Sri Lankan context

Lecture references include Sri Lanka's **Electronic Transactions Act No. 19 of 2006**, **Computer Crime Act No. 24 of 2007**, CSSL Code of Ethics, SLCERT, and—where EU personal data is in scope—GDPR. Sector examples include PCI-DSS for payment-card environments, HIPAA in relevant US healthcare contexts, and TRCSL requirements in Sri Lankan telecommunications. Applicability must be checked for the organization, data, sector, and jurisdiction.

CSSL ethical values highlighted:

1. **Professionalism:** high standards, dignity/respect, and protection of the profession's reputation.
2. **Honesty:** truthful work, no plagiarism/deception, and proper credit.
3. **Competence:** accept qualified work, maintain knowledge, deliver quality.
4. **Professional development:** lifelong learning and knowledge sharing.
5. **Adding value to Sri Lanka:** use ICT for social value, innovation, and national digital development.
6. **Responsibility and integrity:** protect confidentiality, avoid conflicts, and act for clients, employers, society, and public interest.

Best practices include authentication, least privilege, backups and recovery tests, timely patching, awareness, encryption/data protection, documentation, incident response, software asset/license audits, and compliance reviews.

## Exam reminders

- Do not assume that open-source software has no license obligations.
- Distinguish privacy, confidentiality, and security.
- In a scenario answer, identify stakeholders and propose concrete controls, not only the violated rule.
- Treat legal applicability carefully: identify the possible law/standard and recommend verification rather than asserting that every rule applies universally.
