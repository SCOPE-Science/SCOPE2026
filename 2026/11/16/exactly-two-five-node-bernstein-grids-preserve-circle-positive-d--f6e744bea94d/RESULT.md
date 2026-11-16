# Exactly two five-node Bernstein grids preserve circle positive definiteness

## Finding
Let \(0=x_0<x_1<x_2<x_3<x_4=\pi\), and define the degree-four Bernstein sampling operator
\[
(T_{\boldsymbol{x}}f)(\pi u)=\sum_{j=0}^4\binom4j u^j(1-u)^{4-j}f(x_j),\qquad 0\le u\le1.
\]
It maps **every** continuous isotropic positive-semidefinite kernel on the circle to another such kernel if and only if its five nodes are one of the two grids
\[
\boxed{(0,\pi/4,\pi/2,3\pi/4,\pi)}\qquad\text{or}\qquad
\boxed{(0,\pi/3,\pi/2,2\pi/3,\pi)}.
\]
The second grid is nonuniform. Thus the entire one-parameter family of valid four-node cubic grids does **not** persist at degree four: the admissible five-node degree-four grids form exactly two isolated choices.

## Assumptions and scope
The circle has geodesic distance in \([0,\pi]\). An isotropic kernel \(f(d(\theta,\varphi))\) is positive semidefinite on every finite configuration precisely when
\[
f(t)=b_0/2+\sum_{m\ge1}b_m\cos(mt),\qquad b_m\ge0,\quad\sum_{m\ge0}b_m<\infty.
\]
Nodes are strictly ordered and endpoints fixed. The theorem concerns **positive semidefiniteness**, not strict finite-site positivity. The output polynomial is extended evenly and periodically from \([0,\pi]\). Every cosine input \(\cos(mt)\) is an admissible generator. Put \(P_m(u)=(T_{\boldsymbol{x}}\cos(m\cdot))(\pi u)\) and
\[
C_k(P)=2\int_0^1P(u)\cos(k\pi u)\,du,\qquad k\ge0.
\]
The preservation question is exactly the requirement \(C_k(P_m)\ge0\) for every integer \(m,k\ge0\).

## Proof
**1. Endpoint Fourier identity and first symmetry.** For every real polynomial \(P\) of degree at most four, integrating by parts four times gives, for each integer \(k\ge1\),
\[
C_k(P)=2\left\{\frac{(-1)^kP'(1)-P'(0)}{(k\pi)^2}-\frac{(-1)^kP'''(1)-P'''(0)}{(k\pi)^4}\right\}.
\]
Write the interior nodes as \(a,b,c\). For \(m=2j\) even, the Bernstein endpoint derivatives are
\[
P_m'(0)=4(\cos(ma)-1),\qquad P_m'(1)=4(1-\cos(mc)).
\]
Positivity of the coefficients for arbitrarily large **odd** output frequencies \(k\) therefore requires
\[
\cos(2jc)\ge\cos(2ja)\quad\text{for every integer }j\ge1.
\]
Here is an elementary rigidity argument. Put \(v_j=\cos(2jc)-\cos(2ja)\ge0\). Because \(0<a,c<\pi\), geometric-series averages show \(J^{-1}\sum_{j=1}^Jv_j\to0\). Since \(0\le v_j\le2\), also \(J^{-1}\sum v_j^2\to0\). But the averages of squares of two cosine sequences can vanish only when their angular frequencies agree up to sign modulo \(2\pi\): otherwise orthogonality of distinct integer exponential sequences gives a strictly positive limiting mean square. Therefore \(\cos(2c)=\cos(2a)\), hence \(c=a\) or \(c=\pi-a\). Strict ordering rules out the former, so \(c=\pi-a\).

**2. Rigidity of the middle node.** For odd \(m\), let \(s=\cos(ma)\) and \(h=\cos(mb)\). With \(c=\pi-a\), the five input samples are \((1,s,h,-s,-1)\). Their Bernstein polynomial splits into an antisymmetric term (whose even output coefficients vanish) and \(6h u^2(1-u)^2\). The displayed identity gives, for every positive even \(k\),
\[
C_k(P_m)=-\frac{288\cos(mb)}{(k\pi)^4}.
\]
Thus \(\cos((2j+1)b)\le0\) for every \(j\ge0\). These cosines have Cesàro mean zero for \(0<b<\pi\). If \(b\ne\pi/2\), their squares have Cesàro mean \(1/2\), contradicting nonpositivity and zero mean (as \(0\le-\cos((2j+1)b)\le1\)). Hence \(b=\pi/2\) and \(0<a<\pi/2\).

**3. Exact coefficients on the symmetric grid.** The nodes are now \((0,a,\pi/2,\pi-a,\pi)\). Set \(s=\cos(ma)\). When \(m\) is odd, the nonzero-output-parity coefficients are
\[
C_0(P_m)=0,\quad C_k(P_m)=\frac{16}{(k\pi)^4}\big[(1-s)(k\pi)^2+12s-6\big]\quad(k\ge1\text{ odd}),
\]
with all positive even coefficients zero. Their brackets are strictly positive for every \(-1\le s\le1\): for \(k=1\) the minimum is \(2\pi^2-18>0\), whereas for \(k\ge3\) odd the minimum is \(6>0\).

For even \(m\), set \(\varepsilon=(-1)^{m/2}\). All positive odd output coefficients vanish, and
\[
C_0(P_m)=\frac25(2+2s+\varepsilon),\qquad
C_k(P_m)=\frac{16}{(k\pi)^4}\big[(1-s)(k\pi)^2+24s-18\varepsilon-6\big]\quad(k\ge2\text{ even}).
\]
The positive even coefficients are nonnegative for **all** \(s\in[-1,1]\). Indeed if \(\varepsilon=1\), the bracket equals \((1-s)[(k\pi)^2-24]\ge0\); if \(\varepsilon=-1\), it is minimized over \(k\ge2\) and \(s\in[-1,1]\) at \(k=2,s=1\), with value \(36\). The constant coefficient is automatic if \(\varepsilon=1\), and for \(m=4j+2\) its positivity is equivalent to
\[
\cos((4j+2)a)\ge-\tfrac12\qquad\text{for every }j\ge0.
\]

**4. An arithmetic two-grid classification.** Put \(z=e^{2ia}\) and \(w=e^{4ia}\). The preceding condition says that every point in the orbit \(\{zw^j:j\ge0\}\) lies in the closed arc \(\{\operatorname{Re}\zeta\ge-1/2\}\). If \(w\) has infinite order, its orbit is dense and violates the inequality. If its finite order is \(q\ge4\), the orbit contains \(q\) equally spaced points, whose maximal empty circular gap \(2\pi/q\le\pi/2\) is smaller than the forbidden open arc of length \(2\pi/3\), again a contradiction. Thus \(q\le3\). In \(0<a<\pi/2\), order one is impossible, order two gives \(a=\pi/4\), and order three gives \(a=\pi/6\) or \(a=\pi/3\). The first order-three candidate fails at \(j=1\), since \(\cos(6\cdot\pi/6)=-1\). The remaining two choices both obey the inequality for every \(j\): for \(a=\pi/4\) the cosines are zero, while for \(a=\pi/3\) they cycle through \(-1/2,1,-1/2\). All cosine coefficients are therefore nonnegative at precisely these two grids. Nonnegative combinations and uniform limits extend this fact from the cosine generators to every continuous positive-semidefinite isotropic kernel, completing both directions of the classification.

## Verification
All coefficient identities follow from explicit degree-four Bernstein polynomials and four integrations by parts. `CHECK.py` independently expands the polynomial from node values, evaluates endpoint-derivative Fourier formulas, and compares those coefficients to the closed expressions for 65 input frequencies and 48 output modes at each admissible grid (6,240 checks). It also confirms a negative zero-mode coefficient \(-2/5\) for the excluded symmetric grid with \(a=\pi/6\) and input \(\cos(6t)\). These tests are finite corroboration; the proof covers all frequencies and nodes.

## Relationship to prior work
Otten, Nguyen, and Watts established that the standard equispaced Bernstein operator preserves circle positive definiteness in every degree [1], and derived the polynomial endpoint Fourier identity. The present classification allows *arbitrary strictly ordered interior nodes* in degree four, proving both that the uniform grid is not the unique solution and that exactly one nonuniform five-node grid survives. The prior classification of endpoint-fixed node grids in degrees two and three [2] identifies respectively one rigid grid and a continuous one-parameter cubic family; it explicitly does not treat degrees four and above. The arithmetic collapse at five nodes and its exact nonuniform survivor are not consequences of those earlier statements.

## Limitations
No classification is claimed for degree five or higher, repeated nodes, non-Bernstein bases, higher-dimensional spheres, or strict positive definiteness. Literature searches cannot rule out an older equivalent result stated using cosine-positive polynomial interpolation or moment-preserving operators. The finite checker does not certify infinitely many Fourier modes.

## References
[1] M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836, first public 2026-08-05, https://arxiv.org/abs/2608.04836.

[2] *Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-quadratic-rigidity-and-cubic-node-freedom-for-positive-definite--b87f6c90a4aa/RESULT.md.
