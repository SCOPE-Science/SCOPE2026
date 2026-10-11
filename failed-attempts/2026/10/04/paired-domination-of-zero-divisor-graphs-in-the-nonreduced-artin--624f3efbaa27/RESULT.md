# Paired domination of zero-divisor graphs in the nonreduced Artinian regime

## Finding

Let \(R\) be a nonreduced commutative Artinian ring with identity, and write its Artinian decomposition as \[R\cong R_1\times\cdots\times R_k,\qquad k\ge2,\] where each \(R_i\) is local. For the standard zero-divisor graph \(\Gamma(R)\) on the nonzero zero-divisors, the paired-domination number is \[\gamma_{\mathrm{pr}}(\Gamma(R))=2\left\lceil\frac{k}{2}\right\rceil.\] Equivalently, it equals \(k\) when \(k\) is even and \(k+1\) when \(k\) is odd. Thus nilpotent thickness inside the local factors does not affect paired domination; only the number and parity of the Artinian local factors matter.

The statement concerns the nilpotent, nonlocal part of the Artinian classification: at least one local factor is nonreduced, while there are at least two local factors.

## Assumptions and scope

Let
\[
R\cong R_1\times\cdots\times R_k,
\qquad k\ge2,
\]
be the Artinian decomposition into commutative local Artinian rings. Write \(\mathfrak m_i\) for the maximal ideal of \(R_i\). Since \(R\) is nonreduced, at least one factor has nonzero nilradical, but the proof allows both field and nonfield local factors among the \(R_i\).

The standard zero-divisor graph \(\Gamma(R)\) has vertices the nonzero zero-divisors of \(R\); distinct vertices are adjacent exactly when their product is zero.

A paired dominating set is a dominating set whose induced subgraph has a perfect matching. Every paired dominating set is therefore a total dominating set.

## Proof

For each \(i\), choose a nonzero element \(a_i\in R_i\) satisfying
\[
\mathfrak m_i a_i=0.
\tag{1}
\]
Such an element exists for every local Artinian factor. If \(R_i\) is a field, take \(a_i=1\). If it is not a field, its socle \(\operatorname{Ann}(\mathfrak m_i)\) is nonzero; equivalently, the standard Artinian-local argument produces a nonzero element annihilated by the maximal ideal.

Define
\[
x_i=(0,\ldots,0,a_i,0,\ldots,0)\in R,
\]
with \(a_i\) in coordinate \(i\). Because \(k\ge2\), each \(x_i\) is a nonzero zero-divisor. For \(i\ne j\),
\[
x_i x_j=0,
\]
so
\[
D=\{x_1,\ldots,x_k\}
\]
induces a clique.

We first verify that \(D\) totally dominates \(\Gamma(R)\). A tuple \(z=(z_1,\ldots,z_k)\) is a zero-divisor in the finite product precisely when some coordinate is a nonunit. In a commutative local Artinian ring the nonunits are exactly the maximal ideal, so choose \(i\) with \(z_i\in\mathfrak m_i\). By (1),
\[
z x_i=0.
\]
If \(z=x_i\), then \(x_i\) is adjacent to every \(x_j\) with \(j\ne i\). Thus \(D\) is a total dominating set.

Published domination theory gives the matching lower bound for this Artinian regime. For a product of \(k\) local commutative Artinian rings, the ordinary domination number of \(\Gamma(R)\) is \(k\), apart from the field and \(\mathbb Z_2\times F\) field exceptions. Neither exception is nonreduced with \(k\ge2\). Consequently
\[
\gamma_t(\Gamma(R))\ge\gamma(\Gamma(R))=k.
\]
Together with the set \(D\), this gives
\[
\gamma_t(\Gamma(R))=k.
\tag{2}
\]
This equality is used only as a lower bound for the paired parameter.

Every paired dominating set is total dominating and has even cardinality. Hence (2) implies
\[
\gamma_{\mathrm{pr}}(\Gamma(R))
\ge
2\left\lceil\frac{k}{2}\right\rceil.
\tag{3}
\]

If \(k\) is even, the clique \(D\) has a perfect matching, so it is itself paired dominating and equality holds in (3).

Suppose \(k\) is odd. Then \(k\ge3\). Put
\[
y=x_2+x_3.
\]
This is a nonzero zero-divisor because its first coordinate is zero. It is adjacent to \(x_1\), while all the \(x_i\) are mutually adjacent. The set
\[
D\cup\{y\}
\]
has size \(k+1\), dominates because it contains \(D\), and has a perfect matching: match \(y\) with \(x_1\), then pair the remaining \(k-1\) vertices \(x_2,\ldots,x_k\) arbitrarily inside their clique. Thus equality again holds in (3).

Therefore
\[
\gamma_{\mathrm{pr}}(\Gamma(R))
=
2\left\lceil\frac{k}{2}\right\rceil.
\]

## Verification

The standalone `verify.py` constructs several nonreduced products of local rings of the form \(\mathbb Z/p^e\mathbb Z\), builds the standard zero-divisor graph directly from ring multiplication, exhaustively computes total and paired domination minima, and separately checks the socle-supported witness used in the proof.

It includes two-, three-, and four-factor examples, with both field and nonfield local factors.

Exact output:

```text
VERIFY_OK
factors=((2, 2), (2, 1)) vertices=5 gamma_t=2 gamma_pr=2 witness=2
factors=((2, 2), (3, 1)) vertices=7 gamma_t=2 gamma_pr=2 witness=2
factors=((2, 3), (3, 1)) vertices=15 gamma_t=2 gamma_pr=2 witness=2
factors=((2, 2), (2, 1), (2, 1)) vertices=13 gamma_t=3 gamma_pr=4 witness=4
factors=((2, 2), (3, 1), (2, 1)) vertices=19 gamma_t=3 gamma_pr=4 witness=4
factors=((2, 3), (2, 1), (3, 1)) vertices=39 gamma_t=3 gamma_pr=4 witness=4
factors=((2, 2), (2, 1), (2, 1), (2, 1)) vertices=29 gamma_t=4 gamma_pr=4 witness=4
```

These finite calculations are corroborative only. The arbitrary Artinian statement is proved by the socle construction and the published Artinian domination lower bound.

## Relationship to prior work

Anderson and Badawi give the standard zero-divisor graph convention and study zero-divisor graphs from the commutative-algebra side, with primary classification in commutative algebra.

Jafari Rad, Jafari, and Mojdeh study domination, total domination, and connected domination in zero-divisor graphs. Their Artinian result determines the ordinary domination number of a product of local Artinian rings, while their total-domination formulas include the two-factor setting. Their full text does not introduce paired domination.

Kiani, Maimani, and Nikandish later determine total domination much more broadly for Noetherian zero-divisor graphs using maximal associated primes. Their full text likewise treats domination, total domination, and semi-total domination, but not paired domination.

The present result adds the perfect-matching constraint in the nonreduced nonlocal Artinian regime. The new point is that socle elements from the local factors form a canonical dominating clique, so the published total-domination lower bound becomes sharp for paired domination up to exactly the unavoidable parity correction.

Targeted searches for the exact object together with “paired domination,” “paired dominating set,” and “paired domination number” did not locate a covering theorem.

## Limitations

The theorem is restricted to nonreduced commutative Artinian rings with at least two local factors. It does not assert a formula for local rings, where the shape of the nilpotent zero-divisor graph can affect the existence and size of paired dominating sets.

The ordinary and total domination facts used for the lower bound are published results; the contribution here is the exact paired-domination value and its explicit perfect-matching witnesses.

No claim is made for noncommutative zero-divisor graphs or for non-Artinian rings.

## References

1. D. F. Anderson and A. Badawi, “On the Zero-Divisor Graph of a Ring,” *Communications in Algebra* 36 (2008), 3073–3092. DOI: 10.1080/00927870802110888.
2. N. Jafari Rad, S. H. Jafari, and D. A. Mojdeh, “On Domination in Zero-Divisor Graphs,” *Canadian Mathematical Bulletin* 56 (2013), 407–411. DOI: 10.4153/CMB-2011-156-1.
3. S. Kiani, H. R. Maimani, and R. Nikandish, “Some Results on the Domination Number of a Zero-divisor Graph,” *Canadian Mathematical Bulletin* 57 (2014), 573–578. DOI: 10.4153/CMB-2014-027-8.
4. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206.
