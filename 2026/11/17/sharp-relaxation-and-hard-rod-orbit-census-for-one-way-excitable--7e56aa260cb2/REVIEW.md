# Independent mathematical audit

## correctness

PASS

For q>=4 and n>=3, the one-input update makes each new excitation descend from exactly one left neighbor, so excitation lines can only terminate. A first collision comes from an initial excited site at forward distance <q or unrecovered initial phase a>=2 with a+r<=q; a refractory wake from another line would require that line to obstruct first at its initial site. Therefore no surviving line dies after min(n,q-1) steps; residual refractory states clear by q+min(n,q-1)-2. The single-seed witness for n<q and the two seeds at spacing q-1 for n>=q attain this first-periodic-entry cutoff. Noncolliding trains have cyclic excited-site gaps >=q, advance by one per update, and their integer compositions yield R_q(d); shift invariance and Mobius inversion give fixed/primitive temporal periods, while the primitive q-gap transfer has Perron root satisfying lambda^q=lambda^(q-1)+1. Independently enumerated all q^n initial states for (q,n)=(4,3),(4,4),(4,5),(5,3),(5,4),(6,3), with correct max entry, survivor reconstructions, and fixed-word counts; finite checks corroborate, not prove, the unrestricted statement.

## originality

PASS

Directed single-input multi-state pulse sorting admits a new q>=4 sharp global transient clock, explicit survivor criterion and all-primitive-period hard-rod count. The published one-way three-state theorem has the opposite ring orientation and only q=3; its result is a special alphabet and does not establish the q-dependent refractory threshold or sharp all-q entry clock. Symmetric-neighborhood Greenberg-Hastings results operate under different coupling and do not furnish the assigned directed one-input theorem. Best-of-knowledge PASS, with foundational archival access/priority risk.

## value

PASS

A natural family of deterministic excitable cellular automata gains exact worst-case relaxation, initial-state survivor decision, full finite temporal orbit census and entropy. These determine a dynamical classification of all directed one-input rings rather than a routine small finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
