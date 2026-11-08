# Scientific review: cube–segment join positivity cutoff

## Correctness

**PASS.** The object is the standard integral join of a unit \(d\)-cube and a unit segment in \(\mathbb Z^{d+2}\). Slice counting proves the exact expression \(L_d(t)=\sum_{j=0}^{t}(t-j+1)(j+1)^d\). Bernoulli-polynomial expansion provides explicit formulas for every coefficient, including the strict positivity of each coefficient when \(d\le16\), the first negative coefficient \([t]L_{17}=-30301/798\), and a negative coefficient in each dimension \(d\ge18\) selected by the largest \(r\le d\) with \(r\equiv2\pmod4\). The latter relies on the classical even-Bernoulli formula and a stated all-index growth bound. The 1,249 exact-arithmetic checks reproduce the finite identities; they are not substituted for the proof of the infinite range.

## Originality

**PASS, with historical-priority risk.** Liu–Tao–Xin, arXiv:2606.18794v1, Theorem 2.3 and Example 2.4, prove eventual failure for large dilation of a fixed Ehrhart-positive polytope and give a dilated four-cube example. The present result treats *undilated* cubes with dimension varying and completely determines their sharp sign-change boundary. Their Proposition 1.2(iv) provides an Ehrhart-series join identity, but does not imply a dimension-seventeen threshold or the coefficient formulas without new Bernoulli sign analysis. The paper's related section on double sums uses unshifted powers; replacing them by the shifted cube counts changes the coefficient signs. Fu Liu's survey arXiv:1711.09962v2 treats isolated cubes, general positive families and negative examples, not this join family. Targeted publication searches and mathematical-record comparisons identified no covering claim. This does not certify global historical priority.

## Mathematical value

**PASS.** The result resolves a natural and sharply parameterized question for two canonical Ehrhart-positive building blocks with no artificial scaling: exactly when their lattice join loses coefficient positivity. The answer is an unexpected finite boundary at cube dimension seventeen and a theorem for *all* higher dimensions, not a finite sample or a small improvement to a table entry. The explicit Bernoulli sign rule explains why positivity can persist for many dimensions before failing and yields a negative-coefficient witness in every larger dimension. Such a boundary distinguishes the weaker property of Ehrhart-series positivity (preserved by join) from strict monomial-coefficient Ehrhart positivity (not preserved).

## Closest prior work and limits

The main published join result concerns arbitrarily large dilations, rather than the undilated dimension progression. The positivity survey establishes background examples, not the sharp dimension boundary. The theorem is specific to the standard cube–segment join; it does not claim the earliest possible counterexample among *all* joined lattice polytopes or resolve analogous questions for other factors. Its originality assessment remains provisional pending independent expert review.

Self-review: passed. Independent audit: not yet performed.
