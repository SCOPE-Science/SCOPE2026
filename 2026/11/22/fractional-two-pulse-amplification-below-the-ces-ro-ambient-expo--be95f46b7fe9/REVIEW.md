# Review of the two-pulse Cesàro amplification theorem

## Correctness — PASS
The proof is reconstructed from the weighted \(\ell^p\) norm: (i) one-coordinate averages have exact sharp supremum \(1/(1-\alpha q)\); (ii) Tonelli and Jensen show the full best constant is finite; (iii) normalized two-coordinate orbit averages converge to an explicit two-singularity integral; (iv) differentiation at zero and a beta-integral yield a strictly positive fractional boundary layer. Uniform tail bounds at both singularities, with \(\alpha q<1\), justify the limiting steps. Numerical checks in `verify.py` independently test the finite identities, a strict witness, and the beta asymptotics; they are not proofs of universal quantification.

## Originality — PASS, literature-qualified
The closest primary source is Abbar–Arnold–Coine, arXiv:2609.24601v1, Theorem 3.4 and Example 3.10. The former obtains an exact basis test for \(q\ge p\), and the latter obtains the power-weight boundedness range for all \(q\). Neither gives the strict best-constant inequality below \(p\). Arnold, arXiv:2610.00271v1, addresses universal exponent self-improvement. The closest published regularly varying shift finding, identifier `e438690c71d4`, classifies strong and weak exponent endpoints; its full result was inspected and does not compute these sharp subambient constants. Older equivalent mixed-norm Hardy estimates remain a priority risk. A search's failure alone is not treated as novelty proof.

## Mathematical value — PASS
The q-versus-p boundary controls whether normalized basis vectors suffice to determine optimal Cesàro bounds. Showing that they *never* suffice for nontrivial admissible polynomial weights when \(q<p\) is a qualitative structural separation valid throughout an open parameter domain. The exact beta coefficient supplies a quantitative and reproducible mechanism for that separation. The full optimal constant and global optimizer remain unknown.

## Limitations
Scope is \(1\le p<\infty\), \(0<q<p\), \(0<\alpha<1/p\), and pure power weights. The derivation of the strict inequality does not characterize all maximizing vectors. No independent mathematical or bibliographic audit has been performed.

Self-review: passed. Independent audit: not yet performed.
