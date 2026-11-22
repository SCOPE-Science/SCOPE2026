# Self-review

**Correctness — PASS.** The canonical trigonal map has cubic field equation \(U^3-t^4U^2+1=0\). Its squarefree discriminant \(4t^{12}-27\), nontrivial square class and three rational simple poles yield a regular tame \(S_3\)-closure. Riemann–Hurwitz gives genus \(13\). The exact field-root enumeration was executed from the attached standalone `verify.py` and gives \(12\) and \(408\) points over \(\mathbb F_{11}\) and \(\mathbb F_{121}\); equality with Hasse–Weil proves maximality and \(L(T)=(1+11T^2)^{13}\). Scope is the stated smooth projective closure only.

**Originality — PASS, qualified.** Kudo–Harashita (arXiv:1702.05313) and Kudo–Harashita–Senda (arXiv:1709.03627) establish the original genus-four curve, maximality context and its automorphisms. Ogasawara–Ohashi–Sakata–Harashita (arXiv:2403.08139, §4.4) identifies this canonical double-elliptic model. Neither the inspected original results nor the targeted mathematical record search supplies or dominates the exact genus-thirteen \(S_3\)-cover and its maximality. Searches for equivalent cubic/discriminant, genus, field and Frobenius spectrum were made. Unindexed curve tables or alternative presentations remain a residual priority risk.

**Value — PASS.** The natural trigonal Galois closure of a distinguished genus-four curve is a nonabelian degree-six construction producing a maximal genus-thirteen curve, with a new genus-five sign quotient and explicit complete tame ramification/Frobenius data. Superspeciality of the genus-four source alone cannot establish the new maximality.

The Python verifier checks finite arithmetic exhaustively but is not an external formal certificate. No classification of all genus-thirteen maximal curves, complete automorphism group, or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
