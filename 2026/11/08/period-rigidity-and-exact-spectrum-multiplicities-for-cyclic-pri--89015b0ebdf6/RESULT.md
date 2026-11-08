# Period rigidity and exact spectrum multiplicities for cyclic prime-fiber graphs

## Finding

Let \(m\ge1\) be an integer and \(q\ge2\) a **prime** with \(\gcd(m,q)=1\). Write \(H=\mathbb Z/m\mathbb Z\), \(Q=\mathbb Z/q\mathbb Z\), and \(G=H\times Q\). For an arbitrary function \(f:H\to Q\), set
\[
A_f=\{(x,f(x)):x\in H\}\subset G,
\qquad
P_f=\{a\in H:f(x+a)=f(x)\text{ for every }x\in H\}.
\]
For a frequency pair \((s,t)\in H\times Q\), let \(\chi_{s,t}(x,y)=\exp(2\pi i(sx/m+ty/q))\). An **exponential spectrum** of \(A_f\) is an \(m\)-element set of distinct frequencies whose restricted characters form an orthogonal basis of \(\mathbb C^{A_f}\).

**Complete partner classification.** A set \(B\) is a spectrum of \(A_f\) if and only if it is the graph
\[
B_g=\{(s,g(s)):s\in H\}
\]
of a function \(g:H\to Q\) that is constant on every coset of the annihilator
\[
P_f^\perp=\{s\in H:sa\equiv0\pmod m\text{ for every }a\in P_f\}.
\]
In particular, the number of *distinct frequency sets*, without quotienting by translations or automorphisms, is exactly
\[
\boxed{\#\operatorname{Spec}(A_f)=q^{|P_f|}.}
\]

**Complete multiplicity distribution.** For every divisor \(d\mid m\), exactly
\[
\boxed{H_{m,q}(d)=\sum_{\substack{e\mid m\\d\mid e}}\mu(e/d)q^{m/e}}
\]
of the \(q^m\) graph sets have \(|P_f|=d\), and each of these has exactly \(q^d\) distinct spectra. Here \(\mu\) is the number-theoretic Möbius function. The total number of ordered spectral pairs with first set a graph over \(H\) is therefore
\[
\boxed{\sum_{d\mid m}q^d\sum_{\substack{e\mid m\\d\mid e}}\mu(e/d)q^{m/e}.}
\]
These statements apply without a square-free hypothesis on \(m\); hence the cyclic realization \(G\cong\mathbb Z/(mq)\mathbb Z\) includes repeated prime factors.

For example, on the thirty-cycle with \((m,q)=(6,5)\), the entire multiplicity histogram is \((5:15480),\ (25:120),\ (125:20),\ (15625:5)\), giving exactly \(161025\) ordered spectral pairs of six-point graph sets.

## Assumptions and scope

The prime condition on \(q\) and the coprimality condition are essential to the cyclotomic coefficient comparison used here. No regularity, injectivity, additivity, or surjectivity is required of \(f\). Zero frequency and nonzero frequency are treated uniformly; each frequency set is counted once. The character pairing is the explicit product pairing above, which is a relabelling of the usual cyclic Fourier pairing under the Chinese remainder isomorphism. The result makes no claim about sets that do not project bijectively to the \(H\) factor, or about composite fiber orders.

## Proof

**1. Every spectrum is a frequency graph.** If an \(m\)-element orthogonal frequency family contained two different characters \((s,t)\) and \((s,t')\) with the same first coordinate, orthogonality would give
\[
\sum_{x\in H}\exp\!\left(2\pi i(t-t')f(x)/q\right)=0.
\]
Let \(n_j=|f^{-1}(j)|\), for \(j\in Q\). A primitive \(q\)-th root of unity has minimal polynomial \(1+X+\cdots+X^{q-1}\) over \(\mathbb Q\), so the vanishing sum implies \(n_0=\cdots=n_{q-1}=m/q\). This contradicts \(\gcd(m,q)=1\). Hence first frequency coordinates are distinct, and since there are \(m\) of them they run over all \(H\). Write the family as \(B_g\).

**2. Exact orthogonality criterion.** Define the level-set indicator \(F_j(x)=\mathbf1_{\{f(x)=j\}}\). For two distinct first coordinates \(s,t\) put \(h=s-t\ne0\) and \(u=g(s)-g(t)\). Their inner product is
\[
\sum_{j\in Q}\exp(2\pi iuj/q)\sum_{x\in H}F_j(x)\exp(2\pi ihx/m).
\]
If \(u=0\), this equals \(\sum_{x\in H}\exp(2\pi ihx/m)=0\). If \(u\ne0\), the minimal polynomial of a primitive \(q\)-th root over \(\mathbb Q(\exp(2\pi i/m))\) is still \(1+X+\cdots+X^{q-1}\), because \(\gcd(m,q)=1\). Vanishing therefore forces all \(q\) coefficients
\[
\widehat F_j(h)=\sum_{x\in H}F_j(x)\exp(2\pi ihx/m)
\]
to be equal. Their sum is zero because \(h\ne0\), so they must **all be zero**. Conversely, if they are all zero, the original inner product is zero for any \(u\). Thus with
\[
S_f=\{h\in H\setminus\{0\}:\widehat F_j(h)\ne0\text{ for some }j\in Q\},
\qquad J_f=\langle S_f\rangle,
\]
orthogonality is equivalent to \(g(s)=g(t)\) whenever \(s-t\in S_f\). By taking paths under the generators, this is precisely the condition that \(g\) be constant on cosets of \(J_f\).

**3. Identify the subgroup.** A translation \(a\in H\) is a period of every \(F_j\) if and only if
\[
\bigl(\exp(2\pi iha/m)-1\bigr)\widehat F_j(h)=0
\quad\text{for every }h\in H,\ j\in Q.
\]
This is elementary Fourier inversion, valid on any finite cyclic group. It says exactly \(P_f=J_f^\perp\); finite-group double-annihilator duality yields \(J_f=P_f^\perp\). Since \(|P_f^\perp|=m/|P_f|\), there are \([H:J_f]=|P_f|\) independent coset values for \(g\), hence precisely \(q^{|P_f|}\) spectra. Each allowed graph has \(m\) distinct mutually orthogonal characters, so it is automatically a basis.

**4. Count the period strata.** The unique subgroup of \(H\) of order \(e\mid m\) fixes exactly \(q^{m/e}\) functions \(f:H\to Q\), since such functions are constant on its \(m/e\) cosets. If \(H_{m,q}(d)\) counts functions whose **full** period subgroup has order exactly \(d\), this means
\[
q^{m/e}=\sum_{\substack{d\mid m\\e\mid d}}H_{m,q}(d).
\]
Möbius inversion on the divisor lattice gives the stated formula. Summing the product of stratum size and spectra per graph counts all ordered spectral pairs.

## Verification

The optional standalone `CHECK.py` uses exact integer remainders modulo cyclotomic polynomials to test Fourier orthogonality, without floating-point tolerances. In cyclic orders at most fifteen it examines **every** graph and **every** candidate frequency set, without assuming that the latter is a graph. It similarly tests all frequency sets for representatives of every period stratum at cyclic orders eighteen and thirty, enumerates every graph for its period stratum, and verifies the Möbius histogram and pair totals. The analytic argument above, not finite extrapolation, proves the theorem for all \(m\) and \(q\) in scope.

Sample exact counts include \((m,q)=(4,3)\) with multiplicities \((3:72),(9:6),(81:3)\), and \((m,q)=(9,2)\) with multiplicities \((2:504),(8:6),(512:2)\). The latter two examples involve a nonsquare-free spatial factor.

## Relationship to prior work

Tan and Zhang prove that spectral sets in square-free cyclic groups are precisely complete residue transversals. Their cyclotomic coefficient-comparison lemma is used explicitly here; their main result guarantees **existence** of a spectrum but does not give the **full family or exact number of compatible spectra for each individual transversal**. Here the prime-fiber hypothesis permits an exact description, including for cyclic groups whose order is not square-free. Malikiosis and related work develop Fourier-zero and spectral-pair constraints in cyclic groups; the present period-annihilator classification is a specialized exact partner theorem, not a proof of the general Fuglede conjecture.

## Limitations

No claim is made for composite fiber order, for arbitrary non-graph sets, or for stability under perturbations of the character measurements. The proof relies on elementary finite Fourier duality and cyclotomic minimal polynomials; the numerical checks concern specified finite instances only. Prior work on cyclic spectral pairs is broad, and an equivalent periodicity formulation in older literature remains a possible priority risk. No independent mathematical audit has been performed.

## References

1. Tan, H. and Zhang, Y., *Fuglede’s conjecture for cyclic groups of square-free order*, arXiv:2610.02218v1, first public 2026-09-09, Theorem 1.1 and Lemma 2.1.
2. Malikiosis, R. D., *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800, Sections 3 and 8–10 (published in *Forum of Mathematics, Sigma*, 2022).
3. Kiss, G., Malikiosis, R. D., Somlai, G. and Vizer, M., *Fuglede’s conjecture holds for cyclic groups of order pqrs*, *Journal of Fourier Analysis and Applications* (2022), Section 2.1.
