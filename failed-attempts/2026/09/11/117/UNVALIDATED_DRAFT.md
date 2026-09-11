# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the stated 2+2 diagonal pole-control lemma

## Claim under test (target)
Fix spectator weights $(\lambda_2,\lambda_3,\lambda_4)=(3,7,11)$ and let
$\lambda_0,\lambda_1$ vary. Let $S_{22}$ be the summed quintic-twisted virtual
contribution over all fixed loci in $\bar M_{0,0}(\mathbf P^4,4)$ with two
degree-$2$ non-contracted components meeting at a single node over a fixed point
and no contracted component, with standard $1/|\mathrm{Aut}|$ factors.
The claim: $S_{22}$ has at most a simple pole along $\lambda_0=\lambda_1$ with
residue exactly $-125/96$.

## Verdict
**False as stated.** $S_{22}$ is not even a well-defined rational function near
the diagonal at exactly these spectators: 16 of the 80 ordered $2{+}2$ triples
divide by transverse denominator factors that vanish identically in
$(\lambda_0,\lambda_1)$ while their numerators are nonzero. Hence no Laurent
expansion $R_{-1}/(\lambda_0-\lambda_1)+\mathrm{reg}$ exists, and the residue
assertion is void. A secondary exact computation shows the 64 nonsingular terms
alone carry a double pole, so no natural sub-sum recovers the claim either.

## Localization setup (conventions fixed by reproduction of known totals)
We use Graber–Pandharipande virtual localization in genus $0$ for
$\mathbf P^4$ with the quintic twist. For a degree-$d$ edge joining fixed
points $p_i,p_j$ (weights $\lambda_i,\lambda_j$), the Euler sequence gives the
moving weights of $H^0(C_e,f^*T\mathbf P^4)$ as
$(a\lambda_i+b\lambda_j)/d-\lambda_k$ ($a+b=d$) minus the two zero combinations;
the quintic numerator is $e^T(H^0(C_e,f^*\mathcal O(5)))$ with weights
$(c\lambda_i+(5d-c)\lambda_j)/d$. A two-edge chain $(a,m,b)$ contributes
$(Q_1Q_2/E_1E_2)\cdot(V/F)\cdot(w_1u/S)$ with $V=\prod_{j\ne m}(\lambda_m-\lambda_j)$
(normalization subtraction of $T_{p_m}$), $F=5\lambda_m$ (quintic fiber at the
node), $w_1,u$ the tangent weights at the node, $S$ the smoothing weight, and
ordered weight $1/(2d_1d_2)$. Calibration by exact arithmetic:

- $n_1=2875$ reproduced at three generic weight sets;
- $N_2=4876875/8$ reproduced at three generic weight sets, which by the
  Aspinwall–Morrison formula $N_2=n_2+n_1/8$ is equivalent to $n_2=609250$.

Thus the assembly (signs, $|\mathrm{Aut}|$, normalization routing) is correct,
and the resonances below live in the geometry, not in conventions.

## Obstruction 1 — midpoint resonance in degree-2 edge denominators
$(3+11)/2=7$ exactly. For the degree-$2$ edge joining the spectators of weights
$3$ and $11$, the $H^0(\mathbf P^1,\mathcal O(2))$ middle weight
$(\lambda_i+\lambda_j)/2-\lambda_k$ with $k$ the weight-$7$ spectator vanishes.
Concretely the section $st\otimes e_3$ has torus weight $7-7=0$, a genuine extra
fixed direction, so the locus is not an isolated fixed point. Exactly:
$E(2,4)=E(4,2)=0$ identically in $(\lambda_0,\lambda_1)$ (verified at two
distinct $(\lambda_0,\lambda_1)$ pairs), while $Q(2,4)=Q(4,2)=42455111372548875
\ne 0$. Every ordered triple using edge $(2,4)$ or $(4,2)$ as a side (14 triples)
is a genuine pole for all $(\lambda_0,\lambda_1)$. Any correct localization
computation contains this factor; it comes from the $H^0(\mathcal O(2))$ weight
table via the Euler sequence.

## Obstruction 2 — smoothing resonance in spectator-only chains
$(3-7)+(11-7)=0$ exactly. The chains $(2,3,4)$ and $(4,3,2)$ (middle weight $7$,
outers $3,11$) have identically zero node-smoothing denominator with nonzero
numerator: 2 further singular triples.

## Census and consequence
16 of 80 ordered triples are singular with $h$-independent ($h=\lambda_0-\lambda_1$)
zero denominators and nonzero numerators. $S_{22}$ at exactly $(3,7,11)$ is
therefore formally infinite for every $(\lambda_0,\lambda_1)$ near the diagonal:
the presupposition of the Laurent claim fails, disproving the target. The audit
hypothesis that spectators $(3,7,11)$ "keep transverse denominators nonzero" is
arithmetically false. In a transverse slice $\lambda_3=7+e$, the pair
$(2,4,2)+(4,2,4)$ exhibits a non-canceling $1/e^2$ double pole, confirming the
singularity is structural rather than removable.

## Secondary check — regular remainder still doubly singular
Deleting the 16 singular terms, the remaining 64-term sum was Laurent-expanded in
$h$ by exact rational fitting at $t=0$ and $t=5$: the $h^{-2}$ coefficient is
provably nonzero (exact fractions in the certificate), i.e. a double pole. Hence
restricting to the nonsingular graphs does not produce the claimed simple pole
with residue $-125/96$ either.

## Reproduction
`python3 output/artifacts/certify_disproof.py` (stdlib only, exact
$\mathbf Q$-arithmetic) runs 18 checks — $n_1$/$N_2$ calibration, identical
vanishing of $E(2,4),E(4,2)$, nonvanishing of $Q(2,4),Q(4,2)$, the two integer
resonance identities, the 16/80 census, and both double-pole coefficients —
and prints `DISPROOF_OK`.

## Limitations
The disproof refutes the claim at exactly the stated spectators $(3,7,11)$; it
makes no assertion about generic spectators, where a simple pole with some
residue may well hold. The exact value of the regular remainder's double-pole
coefficient is recorded but not given geometric interpretation. The calibration
uses $N_2=4876875/8$ (i.e. $n_2=609250$ via Aspinwall–Morrison) as the accepted
reference total.
