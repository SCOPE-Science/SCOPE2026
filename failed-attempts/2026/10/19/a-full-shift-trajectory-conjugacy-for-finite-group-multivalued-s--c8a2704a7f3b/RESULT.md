# A full-shift trajectory conjugacy for finite-group multivalued shifts

## Finding
Let \(H\) be any finite group acting freely on a nonempty finite alphabet \(A\). Put \(X=A^{\mathbb N_0}\), where \(\sigma\) is the one-sided left shift and \(H\) acts coordinatewise. The multivalued map
\[
F(x)=\{h\cdot\sigma x:h\in H\}
\]
has a complete forward-trajectory space
\[
\mathcal O_F=\{(x^{(t)})_{t\ge0}:x^{(t+1)}\in F(x^{(t)})\}.
\]
Its time-shift dynamical system \((\mathcal O_F,\Theta)\) is topologically conjugate to the one-sided full shift on \(A\times H\).

Writing \(q=|A||H|\), it follows, for every integer \(n\ge1\), that
\[
\#\operatorname{Fix}(\Theta^n)=q^n,\qquad h_{\mathrm{top}}(\Theta)=\log q,\qquad \zeta_\Theta(t)=\frac1{1-qt}.
\]
The number of primitive periodic orbits of least period \(n\) is \(\frac1n\sum_{d\mid n}\mu(d)q^{n/d}\). In particular the binary complement-and-shift map has \(4^n\) periodic trajectories of period dividing \(n\) and trajectory entropy \(\log 4\). These count *complete periodic trajectories*, not points satisfying a multivalued periodicity convention.

## Assumptions and scope
All alphabets and groups are finite and nonempty, with the group acting freely on every letter: \(h\cdot a=a\) implies \(h=e\). No commutativity is assumed. Coordinates start at index \(0\). The action on \(X\) is by a single group element applied to every coordinate. Equip \(\mathcal O_F\) with its compact product topology and let \(\Theta((x^{(t)})_{t\ge0})=(x^{(t+1)})_{t\ge0}\).

## Proof
**1. Unique branch labels.** For every trajectory, there is a unique \(h_t\in H\) with \(x^{(t+1)}=h_t\cdot\sigma x^{(t)}\): if two choices agreed, their action on \(x^{(t)}_1\in A\) would agree, contradicting freeness. Each \(h_t\) depends continuously on the pair \((x^{(t)},x^{(t+1)})\), since the alphabet and group are finite and discrete.

**2. Explicit gauge coordinates.** Let \(h_0,h_1,\ldots\) denote the unique labels and set
\[
y_0=x^{(0)}_0,\qquad y_j=(h_{j-1}h_{j-2}\cdots h_0)\cdot x^{(0)}_j\quad(j\ge1).
\]
Group products are written in their acting order: the rightmost group element acts first. The map \(\Phi((x^{(t)})_{t\ge0})=((y_j,h_j))_{j\ge0}\) is continuous coordinatewise. Given **any** sequence \(((y_j,h_j))_{j\ge0}\in(A\times H)^{\mathbb N_0}\), define
\[
x^{(0)}_0=y_0,\qquad x^{(0)}_j=(h_{j-1}\cdots h_0)^{-1}\cdot y_j\quad(j\ge1),
\]
then recursively \(x^{(t+1)}=h_t\cdot\sigma x^{(t)}\). This constructs a trajectory and an inverse to \(\Phi\), also continuous coordinatewise. Thus \(\Phi\) is a homeomorphism.

**3. Dynamics.** After advancing one time step, the new initial word is \(h_0\cdot\sigma x^{(0)}\), and the new group labels are \(h_1,h_2,\ldots\). Their gauge letter at coordinate \(j\) is
\[
(h_j\cdots h_1)\cdot(h_0\cdot x^{(0)}_{j+1})=y_{j+1}.
\]
The equality holds in arbitrary, including nonabelian, groups. Consequently \(\Phi\circ\Theta=\sigma_{A\times H}\circ\Phi\).

**4. Dynamical counts.** For the full one-sided shift on \(q\) symbols, a point fixed by the \(n\)-th iterate is precisely an arbitrary word of length \(n\) repeated forever, giving \(q^n\). This also yields entropy \(\log q\) and \(\exp(\sum_{n\ge1}q^nt^n/n)=(1-qt)^{-1}\). Möbius inversion gives the displayed primitive-orbit formula. The full shift is topologically mixing and has the uniform Bernoulli measure as its unique measure of maximal entropy, which transport by \(\Phi\).

## Verification
The standalone file `verify.py` exhaustively checks 1,364 periodic codes for \(H=C_2\) with period at most \(5\), and 1,332 periodic codes for the nonabelian left-regular action of \(H=S_3\) with period at most \(2\). It verifies the inverse gauge construction, the one-step shift-identity, coding injectivity and the exact number of periodic codes. The general proof above, not these finite checks, establishes all periods and groups.

## Relationship to prior work
Oliveira's 2026 work on periodic shadowing for set-valued maps studies maps with two branches arising from an involutive isometry and explicitly features the binary complement-and-shift model; it does not state the complete-trajectory conjugacy or the periodic-trajectory and entropy formulas claimed here. Kelly and McGoff study entropy conjugacy for interval Markov multi-maps, a distinct setting with a more general coding framework but without this precise free finite-group coordinatewise action and the explicit nonabelian gauge. Symbolic skew-product recodings are a natural potential precedent; the distinction here is a complete homeomorphic parametrization of every multivalued trajectory, with unrestricted group labels at every step.

## Limitations
Freeness is used to identify a unique branch label; without it this particular full-shift conjugacy may fail (for a trivial action, \(F=\{\sigma\}\) and the trajectory entropy is only \(\log|A|\)). The theorem does not classify periodic *states* under alternative set-valued orbit conventions. The group and alphabet are finite, and no extension to nonfree or infinite actions is asserted. Related earlier symbolic-coding theorems may imply the conjugacy in some specialized form; an exhaustive historical precedence search is not claimed.

## References
1. M. C. Oliveira, *Periodic Shadowing for Set-Valued Maps* (first public version 2026-02-12), arXiv:2602.12399v1, https://arxiv.org/abs/2602.12399.
2. B. P. Kelly and K. McGoff, *Entropy conjugacy for Markov multi-maps of the interval*, Discrete and Continuous Dynamical Systems 40 (2020), DOI:10.3934/dcds.2020353.
