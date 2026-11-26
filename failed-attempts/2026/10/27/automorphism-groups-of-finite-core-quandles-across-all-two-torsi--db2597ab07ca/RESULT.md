# Automorphism groups of finite core quandles across all two-torsion types

## Finding

Let \(A\) be any finite abelian group (written additively), and let \(T(A)\) be its Takasaki, or core, quandle, with operation \(x\triangleright y=2y-x\). Put \(H=2A\), \(C=A/H\), and
\[
t=|H[2]|=|H/2H|,\qquad u=|C|/t.
\]
The quantities \(t,u\) are positive integers. Then
\[
\boxed{|\operatorname{Aut}(T(A))|=|A|\,|\operatorname{Aut}(H)|\,(u-1)!\,(u!)^{t-1}\,t^{ut-1}.}
\]
This includes all finite groups with mixed elementary 2-primary summands and all odd components.

Moreover, this enumeration comes from a **complete normal form**. Choose one representative \(r_c\in A\) for each \(c\in C\), with \(r_0=0\). Every quandle automorphism fixing \(0\) is uniquely specified by \(L\in\operatorname{Aut}(H)\) and elements \(b_c\in A\) for all \(c\in C\), subject to
\[
 b_0=0,\qquad 2b_c=L(2r_c),\qquad
 c\longmapsto b_c+H\ \text{is a permutation of }C.
\]
Its action is \(f(r_c+h)=b_c+L(h)\) for all \(h\in H\). Every other automorphism is uniquely a translation followed by one fixing \(0\).

For every \(m,n\ge1\), the direct product \(R_m\times R_n\) is \(T(C_m\oplus C_n)\). Write \(a=v_2(m)\), \(b=v_2(n)\), with valuation zero for odd integers, and
\[
 u=2^{[a=1]+[b=1]},\qquad t=2^{[a\ge2]+[b\ge2]},\qquad
 H\cong C_{m/\gcd(2,m)}\oplus C_{n/\gcd(2,n)}.
\]
The displayed order formula therefore provides an explicit answer for all even and odd moduli. More sharply, the canonical affine subgroup \(A\rtimes\operatorname{Aut}(A)\) has index
\[
\boxed{\begin{cases}
4,&a\ge2\ \text{and}\ b\ge2,\\
2,&\{a,b\}\ \text{contains }1\ \text{and an integer}\ \ge2,\\
1,&\text{otherwise}.
\end{cases}}
\]
For example, \(R_2\times R_4\) has \(128\) automorphisms, versus \(64\) affine ones. Also \(R_4\times R_6\) has \(768\) automorphisms, versus \(384\) affine ones. The equal-power example \(R_4\times R_4\) has \(6144\) automorphisms and is included as a previously examined boundary, not an independently new case.

## Assumptions and scope

The underlying group \(A\) is finite and abelian; it may be trivial and may contain elements of order two. All groups of permutations and automorphisms are ordinary finite groups. The quandle operation uses \(2y-x\), so the two-variable action is unambiguously right-distributive. The notation \(H[2]\) means elements annihilated by doubling; \(C_m\) denotes a cyclic group of order \(m\), including \(C_1\).

## Proof

**Step 1: the intrinsic translation group.** Right translations are the reflections \(S_y(x)=2y-x\). Their products are
\[
S_yS_z(x)=x+2(y-z).
\]
Thus the displacement group is canonically the translation group by \(H=2A\), and its orbits are the cosets \(C=A/H\). Because the displacement group is characteristic under every quandle automorphism, any quandle automorphism \(f\) fixing \(0\) conjugates translations by \(h\in H\) to translations by \(L(h)\) for a unique group automorphism \(L\) of \(H\). Consequently
\[
f(r_c+h)=b_c+L(h),\quad b_c=f(r_c),\quad b_0=0.
\]
Its bijectivity is equivalent to the map \(c\mapsto b_c+H\) being a permutation of \(C\).

**Step 2: the exact compatibility equation.** For \(x=r_c+h\), \(y=r_d+k\) with \(h,k\in H\),
\[
2y-x=r_c+2(r_d-r_c)+2k-h.
\]
Substituting the normal form into \(f(x\triangleright y)=f(x)\triangleright f(y)\), and cancelling the \(L\)-terms involving \(h,k\), gives
\[
2(b_d-b_c)=L(2(r_d-r_c))\quad\text{for every }c,d\in C.
\]
The case \(c=0\) with \(b_0=r_0=0\) makes these conditions equivalent to \(2b_c=L(2r_c)\) for every \(c\). Conversely these equations, together with bijectivity on cosets and \(L\in\operatorname{Aut}(H)\), imply preservation of all quandle products, so there are no missing automorphisms.

**Step 3: count the coset permutations.** Define a canonical surjective group homomorphism
\[
\delta:C=A/2A\longrightarrow H/2H=2A/4A,\qquad
\delta(a+2A)=2a+4A.
\]
It is well-defined and surjective because \(H=2A\). There are \(t=|H/2H|=|H[2]|\) target points, and every fiber of \(\delta\) has the same cardinality \(u=|C|/t\). Let \(\bar L\) be the automorphism induced by \(L\) on \(H/2H\). If \(\sigma:C\to C\) is the permutation induced by \(c\mapsto b_c+H\), then the compatibility equations are equivalent modulo \(2H\) to
\[
\delta\circ\sigma=\bar L\circ\delta.
\]
Conversely, for every permutation \(\sigma\) satisfying this identity and fixing \(0\), choose a representative \(v_c\in\sigma(c)\). The displayed condition ensures \(L(2r_c)-2v_c\in2H\), so one can choose \(h_c\in H\) with \(2h_c=L(2r_c)-2v_c\). Then \(b_c=v_c+h_c\) is a solution in the correct coset. There are exactly \(|H[2]|=t\) solutions in that coset. At \(c=0\), \(b_0\) is fixed to be zero.

For a fixed \(L\), the permutation \(\sigma\) acts independently on each of the \(t\) fibers of \(\delta\) over the permutation of target points induced by \(\bar L\). The zero fiber has \((u-1)!\) choices because zero must be fixed; each other fiber has \(u!\) choices. Therefore the number of admissible \(\sigma\)'s is
\[
(u-1)!(u!)^{t-1}.
\]
There are \(ut-1\) nonzero cosets, each admitting \(t\) independent choices for \(b_c\), hence \(t^{ut-1}\) choices. The number of automorphisms fixing zero is \(|\operatorname{Aut}(H)|(u-1)!(u!)^{t-1}t^{ut-1}\). Since every translation is a quandle automorphism, multiplying by \(|A|\) proves the order formula.

**Step 4: rank-two affine-index trichotomy.** The odd primary component of \(A=C_m\oplus C_n\) is unchanged when passing to \(H=2A\), so the ratio to the affine subgroup depends only on the exponents \(a=v_2(m)\), \(b=v_2(n)\). On its 2-primary part, there are \(u=2^{[a=1]+[b=1]}\) and \(t=2^{[a\ge2]+[b\ge2]}\). The contribution of the factor between \(|A|\) and \(|\operatorname{Aut}(H)|\) is respectively \(1,2,6,16,64\) in the exhaustive patterns: exactly one valuation \(1\); exactly one valuation at least \(2\); both valuations \(1\); one valuation \(1\) and the other at least \(2\); both valuations at least \(2\). With both valuations zero it is \(1\). In the same cases the ratio \(|\operatorname{Aut}(A)|/|\operatorname{Aut}(H)|\) is \(1,2,6,8,16\), with both zero again \(1\). For these group-automorphism ratios, the standard order formulas give \(|\operatorname{Aut}(C_{2^s})|=2^{s-1}\) for \(s\ge2\), \(|\operatorname{Aut}(C_2^2)|=6\), \(|\operatorname{Aut}(C_{2^a}\oplus C_{2^b})|=2^{3a+b-2}\) for \(1\le a<b\), and \(|\operatorname{GL}_2(\mathbb Z/2^a\mathbb Z)|=6\cdot2^{4(a-1)}\) for \(a\ge1\). Quotienting gives indices \(1,1,1,2,4\), as claimed. Cases with one odd modulus reduce to the single 2-primary cyclic factor.

## Verification

The standalone `verify.py` enumerates all permutations of the underlying quandle for every test instance of cardinality at most eight, independently checks every quandle table relation, and compares the result with the general formula. It also enumerates all allowed coset maps and fiber lifts for \(R_2\times R_4\), \(R_4\times R_4\), and additional cases, without invoking the counting formula to generate the candidates. The complete deterministic run returns `VERIFY_OK`; the new mixed-exponent example \(R_2\times R_4\) has order \(128\). The finite checks do not replace the algebraic argument for arbitrary finite groups.

Run using Python 3 from this directory: `python verify.py`. No external libraries or data files are required.

## Relationship to prior work

Bardakov and Sangare (2026), arXiv:2610.18676, Question 3.5, ask for the automorphism groups of direct products of dihedral quandles when even moduli occur. Their Theorem 3.2 applies to the Latin case and does not cover these even products. Bardakov, Dey and Singh (2016/2017), arXiv:1608.05178, prove the affine formula in the absence of 2-torsion. Bardakov, Nasybullov and Singh (2017), arXiv:1705.10607, analyze inner automorphism groups with 2-torsion and determine the full automorphism group of the single dihedral quandle \(R_4\), not an all-group order formula for \(T(A)\). Salix and Wood (2025), arXiv:2510.26673, give a small-quandle and displacement-group census. The known computation for the equal-exponent family \(C_{2^k}^d\) is a special case of the current formula; the new content includes mixed exponent patterns, the factorial coset-permutation mechanism, and the rank-two index criterion. No novelty is asserted for those pre-established special cases.

## Limitations

The classification applies to finite **abelian** core quandles, not core quandles of arbitrary nonabelian groups, nor general disconnected Alexander quandles with a non-inversion linear operator. The order formula determines group cardinality and a complete explicit permutation normal form but does not present the abstract automorphism group as a canonical semidirect product of standard permutation groups in every case. The prior literature comparison cannot rule out unindexed equivalent calculations.

## References

1. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1 (first public 2026-10-13), especially §3 and Question 3.5, https://arxiv.org/abs/2610.18676.
2. V. G. Bardakov, P. Dey and M. Singh, *Automorphism groups of quandles arising from groups*, arXiv:1608.05178 (2016), §§4,6, https://arxiv.org/abs/1608.05178.
3. V. G. Bardakov, T. Nasybullov and M. Singh, *Automorphism groups of quandles and related groups*, arXiv:1705.10607 (2017), §5, https://arxiv.org/abs/1705.10607.
4. Q. J. M. Salix and P. P. Wood, *More Automorphism Groups of Quandles*, arXiv:2510.26673 (2025), §§3–4, https://arxiv.org/abs/2510.26673.
