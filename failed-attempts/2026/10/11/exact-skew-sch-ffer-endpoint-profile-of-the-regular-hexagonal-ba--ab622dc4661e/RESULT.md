# Exact skew Schäffer endpoint profile of the regular hexagonal Banach plane

## Finding
For the real Banach plane \(X=(\mathbb R^2,N)\), with
\[
N(u,v)=\max\{|u|,|v|,|u-v|\},
\]
the endpoint skew Schäffer constant is, for every real \(\tau\ge0\),
\[
\boxed{S_{X,\infty}(\tau)=\tau+\frac{1}{1+\tau+\tau^2}
=\frac{(1+\tau)(1+\tau^2)}{1+\tau+\tau^2}.}
\]
In particular, \(S_{X,\infty}(1)=4/3\). Near zero its exact expansion is \(1+\tau^3-\tau^4+O(\tau^6)\); thus the first deviation from the value at zero is cubic, not linear or quadratic.

## Assumptions and scope
All vectors and scalars are real. Write \(S_X=\{z\in X:N(z)=1\}\). We use precisely the endpoint of the skew Schäffer constants introduced by Xu and Liu:
\[
S_{X,\infty}(\tau)=\inf_{x,y\in S_X}
\max\{N(x+\tau y),N(\tau x-y)\},\qquad \tau\ge0.
\]
The hexagonal unit ball has consecutive vertices \((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)\). No smoothness, strict convexity or limiting-space assumptions are imposed.

## Proof
Put \(D=1+\tau+\tau^2\) and \(F=\tau+1/D\).

**Attainment.** Take \(x=(1,1/D)\), \(y=(\tau^2/D,1)\). Since \(D\ge1\) and \(0\le\tau^2/D\le1\), both have norm exactly one. Direct calculation gives
\[
x+\tau y=(F,F),\quad \tau x-y=(\tau-\tau^2/D,\ \tau/D-1).
\]
The first coordinate of the second vector is nonnegative and the second is nonpositive. Their difference equals \(F\), so \(N(x+\tau y)=N(\tau x-y)=F\). Therefore \(S_{X,\infty}(\tau)\le F\).

**Exhaustive lower bound.** Let \(x,y\in S_X\) be arbitrary and denote the maximum in the definition by \(z\). The linear isometry \(R(u,v)=(u-v,u)\) cycles the six unit-ball vertices, hence carries any edge to the edge joining \((1,0)\) and \((1,1)\). Acting simultaneously on \(x,y\), we may therefore assume \(x=(1,s)\) with \(0\le s\le1\). The isometry \(Q(u,v)=(u,u-v)\) preserves that edge and exchanges the second and sixth edges and the third and fifth edges. Thus, after possibly applying \(Q\) to both vectors, \(y\) lies on one of four representative consecutive edges:
\[
(1,t),\quad (1-t,1),\quad (-t,1-t),\quad (-1,-t),\qquad 0\le t\le1.
\]
If \(y=(1,t)\), the first coordinate of \(x+\tau y\) is \(1+\tau\), so \(z\ge1+\tau\ge F\). If \(y=(-1,-t)\), the first coordinate of \(\tau x-y\) is \(1+\tau\), so again \(z\ge F\).

For \(y=(1-t,1)\), the three coordinate or coordinate-difference facets of the hexagonal norm yield
\[
z\ge 1+\tau-\tau t,\qquad z\ge s+\tau,\qquad z\ge\tau(1-s)+t.
\]
Take their weighted arithmetic mean with weights \(1/D,\tau^2/D,\tau/D\), respectively. The weights are nonnegative and sum to one; both \(s\) and \(t\) cancel. Consequently
\[
z\ge\frac{(1+\tau)+\tau^3+\tau^2}{D}=F.
\]
For \(y=(-t,1-t)\) instead, the three relevant facet inequalities are
\[
z\ge s+\tau(1-t),\qquad z\ge\tau+t,\qquad z\ge1+\tau(1-s).
\]
This time take weights \(\tau/D,\tau^2/D,1/D\). Both parameters again cancel, giving \(z\ge F\). These four cases exhaust all six edges by the explicit isometries, including their common vertices. Hence every admissible pair satisfies \(z\ge F\), completing the proof.

The expansion follows from the exact identity \((1+\tau+\tau^2)^{-1}=(1-\tau)/(1-\tau^3)\) for \(0\le\tau<1\). In addition, the profile obeys \(S_{X,\infty}(\tau)=\tau S_{X,\infty}(1/\tau)\) for \(\tau>0\), consistent with the symmetric definition.

## Verification
The proof is symbolic for every real nonnegative parameter: the six-edge reduction is exhaustive, each facet is a term of the norm, and the lower certificates use explicit nonnegative weights summing to one. The attaining pair produces equality in both norm terms. The accompanying exact rational checker verifies the edge-symmetry identities, equality certificates and representative rational parameter values; those finite checks are supplementary and are not used to infer universal validity.

## Relationship to prior work
Ying Xu and Qi Liu introduce the skew Schäffer family, prove general bounds, describe its geometric connection to uniform nonsquareness, and calculate values for Hilbert and Lebesgue spaces. Their October 2026 preprint is the source for the invariant and the earliest public motivation used here. The present result computes its complete endpoint parameter profile for the canonical affine-regular hexagonal normed plane, not a Hilbert or Lebesgue space. The general bounds alone yield no exact value: at \(\tau=1\), their universal lower and upper bounds allow values from \(1\) to \(2\), whereas the exact hexagonal value is \(4/3\). Results concerning von Neumann–Jordan, Ptolemy or Banach–Mazur constants on related hexagonal planes are comparisons about different mathematical functionals and do not imply this skew endpoint profile.

## Limitations
This theorem concerns only the endpoint exponent \(t=\infty\) and one real, two-dimensional affine-regular hexagonal norm. It asserts no formula for other outer exponents, all polyhedral Banach planes, or complexifications. Literature searches do not logically exclude a differently phrased earlier equivalent formula; no independent audit has been performed.

## References
1. Ying Xu and Qi Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, publicly submitted 2026-10-02, https://arxiv.org/abs/2610.03050. Invariant definition, universal bounds, geometric properties, and Hilbert/Lebesgue examples.
2. *The lattice Schäffer constant*, arXiv:2505.16775 (2025), https://arxiv.org/abs/2505.16775. Related terminology but a different positive-cone/lattice restriction, not the skew endpoint calculation here.
