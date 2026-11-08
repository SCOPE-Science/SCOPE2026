# Four nodes are necessary and sufficient for exact tight sampling of quadratic Fock polynomials

## Finding

Let \(\mathcal P_2\) be the complex Hilbert space of polynomials \(f(z)=a_0+a_1z+a_2z^2/\sqrt2\), with \(\|f\|^2=|a_0|^2+|a_1|^2+|a_2|^2\). Define \(N_{\rm tight}\) as the smallest number of *distinct* complex nodes \(z_j\) admitting positive numbers \(v_j\) for which the exact Parseval sampling identity \(\|f\|^2=\sum_jv_j|f(z_j)|^2\) holds for all \(f\in\mathcal P_2\). Then
\[
\boxed{N_{\rm tight}=4.}
\]
An explicit extremal design is the origin with weight \(1/2\), together with the three vertices \(\sqrt2,\sqrt2e^{2\pi i/3},\sqrt2e^{4\pi i/3}\), each with weight \(1/6\):
\[
\boxed{\|f\|^2=\frac12|f(0)|^2+\frac16\sum_{j=0}^{2}|f(\sqrt2e^{2\pi i j/3})|^2.}
\]
Thus two sampling radii permit a four-node tight sampling formula, whereas three nodes cannot be tight at any locations or positive weights.

## Assumptions and scope

The norm is the degree-two truncation of the standard Bargmann–Fock norm \(\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}dA(z)\). Every sampling node lies in \(\mathbb C\), and all weights are strictly positive. More generally, for Gaussian-compensated coherent evaluations \(e^{-|z_j|^2/2}f(z_j)\), the same identity uses the positive weights \(w_j=v_je^{|z_j|^2}\): \(w_0=1/2\) and \(w_j=e^2/6\) for the other three nodes. Arbitrary placement and nonuniform positive weights are allowed in the lower bound.

## Proof

The normalized monomials \(e_0(z)=1\), \(e_1(z)=z\), \(e_2(z)=z^2/\sqrt2\) form an orthonormal basis. For the proposed nodes, the cube-root angular sums \(\sum_{j=0}^2e^{2\pi idj/3}=0\) for \(d=\pm1,\pm2\) annihilate all off-diagonal Gram entries. For the diagonal entries the three-node outer ring contributes \(1/2,1,1\) in monomial degrees \(0,1,2\); the origin contributes \(1/2,0,0\). Hence the weighted evaluation Gram matrix is exactly the identity, proving existence with four nodes.

For necessity, a tight sampling frame in a three-dimensional space must have at least three nonzero evaluation vectors. Suppose there were exactly three nodes. In coordinates \((e_0,e_1,e_2)\), its weighted evaluation matrix is a square \(3\times3\) matrix \(A\) satisfying \(A^*A=I\), hence also \(AA^*=I\). Its distinct rows are therefore orthogonal. Positivity of the weights implies that for every pair of distinct nodes \(z_i,z_j\), the reproducing kernel
\[
K_2(z_i,z_j)=1+z_i\overline{z_j}+\frac{(z_i\overline{z_j})^2}{2}
\]
must vanish. The only two roots of \(1+t+t^2/2\) are \(-1+i\) and \(-1-i\). Thus every pair satisfies \(|z_iz_j|=\sqrt2\), so all three nodes have common radius \(|z_j|=2^{1/4}\). For each oriented pair, the phase difference must therefore be \(\pm3\pi/4\) modulo \(2\pi\). Summing the three oriented phase differences around the cycle gives one of \(\pm3\pi/4,\pm9\pi/4\), none an integer multiple of \(2\pi\). This contradicts closure of the cycle. One or two nodes cannot span the three-dimensional space. Thus four is minimal.

## Verification

The included `CHECK.py` evaluates all sixteen monomial Gram entries of the displayed four-node construction and its Gaussian-compensated normalization at floating-point precision, and separately verifies the algebraic obstruction for three nodes by checking the two roots and all eight oriented triangle phase combinations. These finite algebraic checks are redundant confirmations of the displayed exact proof, not substitutes for it. Run `python CHECK.py` with Python 3 standard library.

## Relationship to prior work

Bownik and Yu [1] establish nearly tight discretization of continuous frames for infinite-dimensional settings. They neither formulate nor determine the *minimum cardinality of a positive exactly tight sampling rule* for the three-dimensional Fock-polynomial space. This finding addresses that finite exact-design question. The classical Fock reproducing-kernel formula and the general finite-frame rank argument are standard ingredients, not asserted discoveries. The single-radius conditioning theorem [2] excludes tight one-circle sampling at degree two, but does not establish the global four-node minimum when different radii and arbitrary positive weights are permitted. The constructed formula is a positive Gaussian bidegree-two cubature formula. An equivalent construction could appear under Gaussian cubature or complex moment quadrature terminology; priority is not claimed as independently certified.

## Limitations

The result concerns only the degree-two truncation of the one-variable standard Gaussian Fock space, with point evaluations and positive weights. It does not classify all four-node optimizers, cover arbitrary polynomial degree or multidimensional Fock spaces, or imply exact finite sampling of the full infinite-dimensional Fock space. The four-point identity is constructive; the three-point impossibility is exact. It should not be conflated with unweighted equal-magnitude coherent-state sampling: the displayed nodes have nonuniform positive weights.

## References

[1] M. Bownik and P.-T. Yu, *Uniform discretization of continuous frames*, arXiv:2603.10423v1, first public 2026-03-11. https://arxiv.org/html/2603.10423

[2] *Sharp one-circle coherent-frame conditioning and angular-design rigidity*, published mathematical record (2026). https://github.com/published-finding corpus/2026
