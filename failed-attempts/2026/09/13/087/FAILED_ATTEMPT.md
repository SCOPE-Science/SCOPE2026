# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Descendant two-contact scattering correspondence for (F1, H plus 2H-E)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1664
- **Disposition:** AUDIT_1_REJECT
- **Domain:** log Gromov-Witten theory and mirror symmetry
- **Method:** descendant tropical correspondence and descendant wall-crossing

## Problem

Let X=F1 be the first Hirzebruch surface realised as the blowup pi:F1->P^2 at one point with exceptional curve E, and let D=D1+D2 where D1=pi^*L for a line L not through the blown-up point (class H) and D2 is the strict transform of a smooth conic through the blown-up point meeting L transversely away from it (class 2H-E), so D is anticanonical with two smooth components meeting transversely in two points. For each effective class beta=aH-kE with a>=2 and 0<=k<=a let c1=beta.D1=a and c2=beta.D2=2a-k, and let Db_beta be the genus-zero log Gromov-Witten invariant of (X,D) with two relative markings of maximal contact orders c1 to D1 and c2 to D2 and one interior marking carrying a point insertion plus psi^{m(beta)}, where m(beta)>=0 is the unique exponent giving a zero-dimensional virtual cycle by the standard log virtual-dimension formula (explicitly computable from beta; non-negative on this subfamily). Prove or disprove that for every such beta, Db_beta equals the coefficient prescribed by the consistent completion of the explicit two-initial-wall descendant scattering diagram on the dual intersection complex of (X,D), equivalently the descendant tropical count with one higher-valency vertex and the associated descendant broken-line product, via descendant tropical correspondence and wall-crossing. A complete answer is a proof for all admissible beta or a rigorous counterexample at one explicit beta0 with both sides computed and unequal.

## Attempted claim

Let X=F1 be the first Hirzebruch surface realised as the blowup pi:F1->P^2 at one point with exceptional curve E, and let D=D1+D2 where D1=pi^*L for a line L not through the blown-up point (class H) and D2 is the strict transform of a smooth conic through the blown-up point meeting L transversely away from it (class 2H-E), so D is anticanonical with two smooth components meeting transversely in two points. For each effective class beta=aH-kE with a>=2 and 0<=k<=a let c1=beta.D1=a and c2=beta.D2=2a-k, and let Db_beta be the genus-zero log Gromov-Witten invariant of (X,D) with two relative markings of maximal contact orders c1 to D1 and c2 to D2 and one interior marking carrying a point insertion plus psi^{m(beta)}, where m(beta)>=0 is the unique exponent giving a zero-dimensional virtual cycle by the standard log virtual-dimension formula (explicitly computable from beta; non-negative on this subfamily). Prove or disprove that for every such beta, Db_beta equals the coefficient prescribed by the consistent completion of the explicit two-initial-wall descendant scattering diagram on the dual intersection complex of (X,D), equivalently the descendant tropical count with one higher-valency vertex and the associated descendant broken-line product, via descendant tropical correspondence and wall-crossing. A complete answer is a proof for all admissible beta or a rigorous counterexample at one explicit beta0 with both sides computed and unequal.

## Research outcome

Proved the descendant two-contact scattering equality for all admissible beta on (F1,H+2H-E): virtual dimension forces m=0 so the claim reduces to the primary toric-model correspondence plus ordinary wall-crossing, both of which apply.

## Why this attempt failed

Failed axes: originality, value.

originality: Fused 3-direction live search (20 results, full provider coverage, no partial failure) finds no prior record of the exact (F1,H+2H-E, aH-kE) equality, but finds broader theorems that substantively imply it. Arguz-Bousseau proves Frobenius structure for blow-ups of toric varieties; Gross-Siebert Intrinsic Mirror Symmetry proves general punctured-invariant mirror ring; Bousseau-Brini-van Garrel treats nef Looijenga pairs; Mandel/Mandel-Ruddat treat descendant/log-tropical correspondence. Draft itself reduces headline to primary (m=0) ordinary correspondence and cites these as established. A prior source need not state headline verbatim: the general toric-model primary correspondence exhaustively covers this subfamily, so headline is a corollary/repackaging of a known stronger fact. Originality FAILS. value: Even though correct, the result is not independently worth retrieving under STANDARD. The only new computation is vdim/m=0 trivialization, i.e. the advertised descendant problem is vacuous on this subfamily (psi^0 sector). No exact invariant value Db_beta is computed, no boundary changed, no classification/census completed, no downstream use shown. What remains is application of already-published general correspondence to one natural-but-arbitrary subfamily aH-kE, a textbook corollary/parameter instance mechanically implied by standard results. The narrow-exact-datum allowance does not apply because no precise value, witness, or constant is established for future use. Value FAILS.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof composes cited established theorems (ACGS decomposition, Nishinou-Siebert toric correspondence, Kontsevich-Soibelman/Gross-Siebert consistency, GHK broken-line dictionary, Bousseau/Gross-Siebert genus-0 Frobenius correspondence) which are not re-proved here; residual risk resides in those published results. No brute-force numeric values of Db_beta are computed; equality is structural. The argument uses the m=0 degeneracy specific to this two-maximal-contact plus point setup and does n…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
