# Complete prime-power word fibers and power-image subgroup thresholds in cyclic regular wreath groups

## Finding

Let \(p\) be any prime, let \(q=p^f\) with \(f\ge 1\), let \(a\ge1\), and let \(n=p^a\). Write
\[
G=\mathbb F_q^n\rtimes_T C_n,
\]
where \(T\) cyclically shifts the coordinates of \(\mathbb F_q^n\). Set \(N=T-I\), so that \(N\) is a single nilpotent Jordan block of size \(n\) over \(\mathbb F_q\), and let
\[
R_b(w,j)=\#\{g\in G:g^{p^b}=(w,j)\},\qquad P_b=\{g^{p^b}:g\in G\}.
\]
Here \(j\in\mathbb Z/n\mathbb Z\) and \(w\in\mathbb F_q^n\). For every \(1\le b\le a\), the following rules give **every prescribed-target fiber**:

* If \(j\neq0\) and \(p^b\nmid j\), then \(R_b(w,j)=0\).
* If \(j\neq0\), \(p^b\mid j\), and \(s=v_p(j)\in\{b,\ldots,a-1\}\), put \(m_s=p^{s-b}(p^b-1)\). Then
  \[
  R_b(w,j)=\begin{cases}p^bq^{m_s},&w\in N^{m_s}\mathbb F_q^n,\\0,&\text{otherwise}.\end{cases}
  \]
* If \(j=0\), put \(e_b=n-p^{a-b}\). Then
  \[
  R_b(w,0)=\begin{cases}
  (p^b-p^{b-1})q^{e_b}+p^{b-1}q^n,&w=0,\\
  (p^b-p^{b-1})q^{e_b},&0\ne w\in N^{e_b}\mathbb F_q^n,\\
  0,&w\notin N^{e_b}\mathbb F_q^n.
  \end{cases}
  \]

For \(b\ge a+1\), every \(p^b\)-th power is the identity, with \(R_b(0,0)=|G|=p^a q^{p^a}\). In particular, for \(1\le b\le a\),
\[
\boxed{|P_b|=q^{p^{a-b}}+\sum_{s=b}^{a-1}(p-1)p^{a-s-1}q^{p^a-p^{s-b}(p^b-1)}.}
\]
The terminal image \(P_a\) is a central subgroup of size \(q\), and \(P_{a+1}=\{1\}\); the group exponent is exactly \(p^{a+1}\). **The set \(P_b\) is a subgroup if and only if \(b\ge a\)** (for positive integers \(b\)). For each fixed \(p,q,b\), the image density has the explicit positive limit as \(a\to\infty\):
\[
\boxed{\lim_{a\to\infty}\frac{|P_b|}{|G|}
=\frac{p-1}{p^{b+1}}\sum_{t=0}^{\infty}p^{-t}q^{-p^t(p^b-1)}.}
\]

## Assumptions and scope

The wreath product is the **regular** one, with the top cyclic group acting by a single length-\(n\) cycle on the base. The additive base may have elementary abelian rank \(f>1\) at each site. All fields have characteristic \(p\), and no restriction to odd characteristic is imposed. Group multiplication is \((v,i)(u,j)=(v+T^i u,i+j)\). The valuation \(v_p(j)\) for nonzero residue \(j\pmod{p^a}\) means the unique integer in \(\{0,\ldots,a-1\}\) independent of the chosen integer representative. The notation \(N^0\mathbb F_q^n\) means the full base group. The image \(P_0=G\) is a subgroup, but the subgroup dichotomy above is stated for \(b\ge1\).

## Proof

**Cyclic module.** The shift representation on the standard coordinate basis identifies the base \(V=\mathbb F_q^n\) with the regular module \(\mathbb F_q[X]/(X^n-1)\), in which \(T\) acts by multiplication by \(X\). Since \(n=p^a\) and the characteristic is \(p\), \(X^n-1=(X-1)^n\). Therefore \(N=T-I\) has a single nilpotent Jordan block of length \(n\), and for \(0\le m\le n\),
\[
\dim_{\mathbb F_q}N^mV=n-m,\qquad |\ker N^m|=q^m.
\]

**Power operator and its image.** By repeated semidirect multiplication, for \(k=p^b\) one has
\[
(v,i)^k=(S_{k,i}v,ki),\qquad
S_{k,i}=\sum_{r=0}^{k-1}T^{ri}=(T^i-I)^{k-1},
\]
where the last polynomial identity follows from \((Y-1)^k=Y^k-1\) in characteristic \(p\). For \(i\ne0\), let \(t=v_p(i)\). We can factor
\[
T^i-I=(T-I)^{p^t}U_i(T),
\]
where \(U_i(T)\) is invertible, since its value at \(T=I\) is the nonzero residue of \(i/p^t\) modulo \(p\). Thus \(S_{p^b,i}\) has image \(N^{m}V\) and kernel size \(q^{\min(m,n)}\), where \(m=p^t(p^b-1)\). If \(i=0\), the power operator is zero. If \(t\ge a-b+1\), then \(m\ge n\), and the power operator is zero as well.

**Nonzero top targets.** For \(j\ne0\), solutions of \(p^bi=j\) in \(C_n\) exist precisely when \(p^b\mid j\) (assuming \(b\le a\)); in that case there are exactly \(p^b\) preimages \(i\). If \(v_p(j)=s\), all these have \(v_p(i)=s-b\), so all corresponding maps \(S_{p^b,i}\) have the same image \(N^{m_s}V\) and every fiber over that image has size \(q^{m_s}\). Summing over the \(p^b\) top preimages proves the first two rules.

**Zero top target.** There are \(p^b\) solutions of \(p^bi=0\). Exactly \(p^b-p^{b-1}\) of these satisfy \(v_p(i)=a-b\); their power operators have common image \(N^{e_b}V\), because
\[
p^{a-b}(p^b-1)=p^a-p^{a-b}=e_b.
\]
Each such operator has kernel cardinality \(q^{e_b}\). The remaining \(p^{b-1}\) top preimages (including \(i=0\)) have zero power operator; they contribute \(q^n\) roots apiece to the identity and none to other targets. This yields every zero-top fiber and the three prescribed-root rules.

**Image sizes, terminal subgroup, and exponent.** There are \((p-1)p^{a-s-1}\) nonzero top residues of valuation \(s\). Their image fibers have size \(q^{n-m_s}\). The zero-top fiber has size \(q^{n-e_b}=q^{p^{a-b}}\), giving the displayed sum. For \(b=a\), only the zero-top coset remains, and its base image is \(N^{n-1}V\), the one-dimensional fixed-point space of \(T\), which lies in the center; hence \(|P_a|=q\). For \(b\ge a+1\), \(p^bi=0\) and every power operator vanishes, so \(P_b\) is trivial. Taking \(i=1\) and a vector \(v\) with nonzero coordinate sum makes \((v,1)^{p^a}\ne1\), so the exponent is exactly \(p^{a+1}\).

**Sharp failure of subgroup closure.** Suppose \(1\le b<a\). The projection of \(P_b\) onto the top group contains \(0\) and \(p^b\), and is exactly \(p^bC_n\). Its fiber above zero has size \(q^{p^{a-b}}\); above \(p^b\) it has size \(q^{n-(p^b-1)}\). Their ratio is
\[
q^{\,(p^b-1)(p^{a-b}-1)}>1.
\]
A subgroup projecting onto a cyclic subgroup has equally large fibers over each point of that image, by multiplication with a fixed lift. The unequal sizes rule out subgroup closure. Conversely, \(P_a\) and all later images are subgroups.

**Asymptotic density.** Divide the exact image formula by \(|G|=p^a q^{p^a}\) and substitute \(t=s-b\):
\[
\frac{|P_b|}{|G|}=\frac{q^{p^{a-b}-p^a}}{p^a}
+\frac{p-1}{p^{b+1}}\sum_{t=0}^{a-b-1}p^{-t}q^{-p^t(p^b-1)}.
\]
The first term tends to zero, and the nonnegative series converges absolutely, proving the stated limit. All conclusions are exact for their specified domains.

## Verification

The included `check_power.py` enumerates the elements of each small wreath group explicitly, raises each group element by repeated group multiplication, and constructs every prescribed-target power fiber. It independently predicts the fibers using coordinate-shift-difference images (without relying on the predicted powers to compute these images). The captured output in `check_power.out` reports **22 complete cases passed** over \(p=2,3,5\), base field sizes \(q=2,3,4,5,9\), top lengths \(n=2,3,4,5,8\), and both terminal and nonterminal depths. In particular, for \(p=q=2\), \(a=3\), the successive image cardinalities at depths \(b=1,2,3,4\) are \(336,36,2,1\), respectively. Exhaustive finite checks are only independent sanity tests; the proof above establishes the whole infinite family.

Reproduction: run `python3 check_power.py` from the directory containing the two standalone artifacts. There are no external Python dependencies.

## Relationship to prior work

Riedl (2009), especially Section 4, develops the regular cyclic-by-cyclic wreath-product group and invokes the standard P. Hall semidirect-power identity; its main theorems characterize automorphisms, not complete root fibers or power-image subgroups. Riedl (2014) studies upper central series of related regular wreath \(p\)-groups, but no full text was available for comprehensive comparison; its abstract and publisher preview concern structural central series rather than power-word counts. Kundu and Mondal (2020) analyze prime-power membership and conjugacy-class counts in the larger symmetric-top wreath product \(H\wr S_n\); the present theorem concerns a restricted cyclic top group and gives **each prescribed target's root multiplicity for all \(p^b\)**, not just counts or conjugacy classes of powers.

The known \(C_p\wr C_p\) element-order and \(p\)-th power identity-fiber calculation is a genuine special case of the general norm operator above and is not claimed as new. Previously published power-fiber results for radical-square-zero quiver unit groups cover different groups and do not imply the cyclic-regular-wreath filtration. The contribution assessed here is the **all-depth, all-target** finite-field family, its exact varying image strata, the non-subgroup cutoff, and the explicit large-depth image-density series. No claim of absolute priority over unindexed historical literature is made.

## Limitations

The theorem uses the elementary-abelian characteristic-\(p\) base with a cyclic regular action; it does not extend without modification to non-elementary abelian base groups, arbitrary top permutation groups, or exponents other than prime powers. The 2014 upper-central-series full text was not accessible, and unindexed or implicitly equivalent power-map results may exist. The comparisons establish the stated distinction from inspected sources, not an independently certified novelty verdict. No independent mathematical audit has been performed.

## References

1. J. M. Riedl, *Automorphisms of Regular Wreath Product p-Groups*, *International Journal of Mathematics and Mathematical Sciences* (2009), Article 245617. DOI: `10.1155/2009/245617`, first published 24 November 2009. Full text: https://onlinelibrary.wiley.com/doi/10.1155/2009/245617.
2. J. M. Riedl, *Upper central series for elementary-abelian-over-cyclic regular wreath product p-groups*, *Journal of Algebra and Its Applications* **14** (2015), 1550044. DOI: `10.1142/S0219498815500449`, first made public 20 October 2014 (publisher preview).
3. R. Kundu and S. Mondal, *Powers in the wreath product of \(G\) with \(S_n\)*, arXiv:`2010.04954v1`, 10 October 2020.
4. Published related result, *Complete power-map fibers in radical-square-zero quiver unit groups* (2026), distinct group family.
5. Published related result, *A sharp order cutoff for the second cyclic-subgroup maximum of odd prime-power groups* (2026), especially the standard \(C_p\wr C_p\) element-order calculation.
