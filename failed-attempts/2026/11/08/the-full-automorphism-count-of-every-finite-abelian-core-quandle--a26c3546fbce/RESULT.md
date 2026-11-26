# The full automorphism count of every finite abelian core quandle

## Finding

Let \(G\) be any finite abelian group and let \(T(G)\) be its core (Takasaki) quandle, with operation \(x*y=2y-x\). In the elementary-divisor decomposition of the Sylow \(2\)-subgroup of \(G\), let \(s\) be the number of cyclic factors of order exactly \(2\), and let \(t\) be the number of cyclic factors of order at least \(4\), counted with multiplicity. Put \(B=2G\), \(h=2^s\), and \(k=2^t\). Then

\[
\boxed{\left|\operatorname{Aut}(T(G))\right|=|G|\,|\operatorname{Aut}(B)|\,k^{hk-1}(h-1)!\,(h!)^{k-1}.}
\]

This is an exact formula for every finite abelian group, with no restrictions on the exponents or the odd-order factor. Here \(0!=1\). The group order \(|\operatorname{Aut}(B)|\) has the standard explicit primary-decomposition formula recorded below, so the expression depends only on the invariant factors of \(G\).

A complete parameterization underlies the count. Choose a transversal \(c\mapsto r_c\in G\) for the cosets \(C=G/2G\), with \(r_0=0\). Every quandle automorphism is uniquely a translation followed by a normalized map \(f\) of the following form:

\[
f(r_c+z)=a_c+g(z)\quad (c\in C,\ z\in 2G),
\]

where \(g\in\operatorname{Aut}(2G)\), \(a_0=0\), and the chosen \(a_c\in G\) satisfy \(2a_c=g(2r_c)\) and have pairwise distinct images modulo \(2G\). Conversely, every such collection defines a quandle automorphism. In particular, this construction determines every automorphism, not only the number.

For any positive integers \(m,n\), the direct product of the dihedral quandles \(R_m\times R_n\) is \(T(C_m\oplus C_n)\), so the theorem gives its full automorphism-group order, including all even-even and even-odd cases. For instance,

\[
|\operatorname{Aut}(R_2\times R_4)|=128,\qquad
|\operatorname{Aut}(R_2\times R_8)|=512,\qquad
|\operatorname{Aut}(R_4\times R_4)|=6144.
\]

The last special case was previously computed and is **not** independently claimed as new. The present assertion is the unrestricted formula and classification, especially its factorial contributions from order-two cyclic factors.

## Assumptions and scope

The group \(G\) is finite, additive and abelian. For \(G=0\), the formula gives one automorphism. The Sylow \(2\)-subgroup decomposes as

\[
G_{(2)}\cong C_2^s\oplus \bigoplus_{i=1}^{t} C_{2^{e_i}},\qquad e_i\ge2.
\]

Write \(U=G/2G\), so \(|U|=2^{s+t}=hk\). The map

\[
\theta:U\longrightarrow 2G/4G,\qquad \theta(x+2G)=2x+4G
\]

is a well-defined surjective homomorphism with kernel of cardinality \(h=2^s\). The target has cardinality \(k=2^t\). These facts follow directly from the displayed primary decomposition; the odd-order component contributes neither to \(U\) nor to \(2G/4G\).

For explicit numerical evaluation of \(|\operatorname{Aut}(2G)|\), decompose each primary part of \(2G\) as \(\bigoplus_i C_{p^{\lambda_i}}\), and let \(m_j\) count the parts of exponent exactly \(j\). The standard finite-abelian-group formula is

\[
|\operatorname{Aut}(2G)|=\prod_p\left(p^{\sum_{i,l}\min(\lambda_i,\lambda_l)}\prod_{j\ge1}\prod_{v=1}^{m_j}(1-p^{-v})\right).
\]

Empty factors have value one.

## Proof

**Step 1: the core identity and its converse.** If \(f:T(G)\to T(G)\) is a quandle automorphism, translate its outputs to arrange \(f(0)=0\). Preservation of \(2y-x\), first with \(y=0\) and then with \(x=0\), gives

\[
f(-x)=-f(x),\qquad f(2y)=2f(y).
\]

Consequently, for all \(x,y\in G\),

\[
f(x+2y)=f(2y-(-x))=2f(y)+f(x).
\]

This identity was already observed by D. Joyce in the proof of his 1979 core-isomorphism proposition. It is used here as an established starting point, not claimed as new. Since \(f(2G)=2G\), its restriction \(g=f|_{2G}\) is a bijection. The identity above shows that \(g\) is additive on \(2G\), so \(g\in\operatorname{Aut}(2G)\).

Choose representatives \(r_c\) as specified. The same identity gives the unique representation

\[
f(r_c+z)=a_c+g(z),\quad a_c=f(r_c),\quad 2a_c=g(2r_c),\quad a_0=0.
\]

A bijection must map the cosets of \(2G\) bijectively, hence the \(a_c+2G\) are distinct.

Conversely, suppose these conditions hold. The piecewise formula is bijective because each coset is mapped bijectively through \(g\), and the output cosets are distinct. For \(x=r_c+z\) and \(y\in G\), the formula gives

\[
f(x+2y)=f(x)+g(2y)=f(x)+2f(y).
\]

Moreover, \(-x=r_c-2r_c-z\), so

\[
f(-x)=a_c-g(2r_c)-g(z)=-a_c-g(z)=-f(x).
\]

Combining these identities gives \(f(2y-x)=2f(y)-f(x)\) for all \(x,y\), proving that the constructed bijection is a quandle automorphism. An arbitrary translation is also a quandle automorphism, and every quandle automorphism has a unique translation-normalized factorization.

**Step 2: permissible induced coset permutations.** Fix \(g\in\operatorname{Aut}(2G)\). The induced permutation \(\sigma:U\to U\) of the normalized map must fix \(0\). If \(\bar g\) denotes the induced automorphism of \(2G/4G\), doubling the identity \(2a_c=g(2r_c)\) shows that

\[
\theta\circ\sigma=\bar g\circ\theta.
\]

Conversely, this relation suffices for lifting any given \(\sigma(c)\) to a compatible \(a_c\): the congruence says that \(g(2r_c)-2r_{\sigma(c)}\in4G=2(2G)\), so choose \(z_c\in2G\) with \(2z_c=g(2r_c)-2r_{\sigma(c)}\) and put \(a_c=r_{\sigma(c)}+z_c\). The group of solutions for \(z_c\) is the kernel \((2G)[2]\), of order \(k\). At \(c=0\), the normalization forces \(a_0=0\), leaving no choice.

The map \(\theta\) has \(k\) fibers, each of cardinality \(h\). For a fixed \(g\), condition \(\theta\sigma=\bar g\theta\) permits any bijection between each fiber of \(\theta\) and the prescribed corresponding fiber. The zero fiber must carry \(0\) to \(0\), giving \((h-1)!\) possibilities, while each of the remaining \(k-1\) fibers allows \(h!\). Thus the number of compatible permutations is exactly

\[
(h-1)!\,(h!)^{k-1}.
\]

For each such permutation there are independently \(k\) choices of \(a_c\) for each of the \(hk-1\) nonzero cosets. The total number of normalized quandle automorphisms above a fixed \(g\) is therefore

\[
k^{hk-1}(h-1)!\,(h!)^{k-1}.
\]

There are \(|\operatorname{Aut}(2G)|\) choices of \(g\), and \(|G|\) independent output translations. Multiplication gives the claimed exact formula.

**Step 3: dihedral products.** Coordinatewise application of \(x*y=2y-x\) identifies \(R_m\times R_n\) with \(T(C_m\oplus C_n)\). Substituting the elementary-divisor decomposition of \(C_m\oplus C_n\) yields the asserted formula for every pair of moduli.

## Verification

The accompanying standalone script `verify.py` implements the core operation directly on finite products of cyclic groups, enumerates all permutations when the group has at most eight elements, and independently tests the core identity on every ordered pair. For twelve finite groups it also computes \(|\operatorname{Aut}(2G)|\) by an independent additive-bijection enumeration and applies the formula. For four groups, it constructs every normalized map in the stated parameterization and checks the quandle law on all ordered pairs: \(C_2\oplus C_4\), \(C_2\oplus C_8\), \(C_4\oplus C_4\), and \(C_2\oplus C_4\oplus C_3\). All tests passed; actual output is in `verification_output.txt`.

These finite computations are checks, not the proof for arbitrary finite abelian groups. The unrestricted result follows from the argument above.

## Relationship to prior work

Bardakov and Sangare (October 13, 2026), Section 3 and Question 3.5, treat products of odd-order dihedral quandles and explicitly ask for automorphism groups of products involving even moduli. Their Latin-quandle centralizer method does not apply when doubling is noninvertible. The present theorem answers that question for all products of two cyclic dihedral quandles and in fact all finite abelian core quandles.

Bardakov, Nasybullov and Singh (2017), Section 5, describe the holomorph for odd-order abelian groups, the full automorphism group for a single order-four dihedral quandle, and inner automorphism groups for many even groups; their results do not state the above unrestricted factorial enumeration. Elhamdadi, Macquarrie and Restrepo (2012) classify the full automorphism group of one cyclic dihedral quandle, not arbitrary Cartesian products.

Joyce (1979, typeset edition 2009), Section 3.3, proves the key normalized identity \(f(x+2y)=f(x)+2f(y)\) while establishing that finite abelian groups with isomorphic core quandles are isomorphic. The identity is deliberately credited as an existing ingredient; the new work is the complete coset-lift classification and count including the mixing of order-two factors.

A previously recorded result already gives \(\operatorname{Aut}(T(C_4^r))\) and its fixed-point distribution, which is included here as a covered special case and not presented as independently new. The unrestricted formula does not follow as a numerical statement from that restricted family because order-two direct summands introduce the new factorial fiber-permutation terms and different higher cyclic exponents change \(\operatorname{Aut}(2G)\).

## Limitations

The theorem is only for finite **abelian** group cores, not nonabelian core quandles or arbitrary Alexander quandles. It determines the order and every automorphism through finite group data; it does not assert a uniform split abstract group presentation for every \(G\). Existing partial classifications of even quandles, including older theses, could provide implicit equivalent enumerations under other terminology; this remains a historical-priority risk requiring independent literature review. The historical-priority comparison is qualified by the scope of sources inspected.

## References

1. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1 (first public 2026-10-13), Section 3, Question 3.5. https://arxiv.org/abs/2610.18676
2. V. G. Bardakov, T. R. Nasybullov and M. Singh, *Automorphism groups of quandles and related groups*, arXiv:1705.10607v3 (2017), Section 5. https://arxiv.org/abs/1705.10607
3. D. E. Joyce, *An Algebraic Approach to Symmetry with Applications to Knot Theory*, dissertation (1979), typeset 2009 edition, Section 3.3. https://aleph0.clarku.edu/~djoyce/quandles/aaatswatkt.pdf
4. M. Elhamdadi, J. Macquarrie and R. Restrepo, *Automorphism Groups of Quandles*, Journal of Algebra and Its Applications 11 (2012), 1250008, doi:10.1142/S0219498812500089.
5. V. G. Bardakov, P. Dey and M. Singh, *Automorphism groups of quandles arising from groups*, arXiv:1608.05178 (2016), for the no-2-torsion setting. https://arxiv.org/abs/1608.05178
