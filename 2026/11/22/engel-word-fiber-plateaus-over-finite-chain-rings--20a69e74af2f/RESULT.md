# Engel-word fiber plateaus over finite chain rings

## Finding
Let \(R\) be any finite commutative chain ring of length \(\ell\geq1\) with residue field of size \(q\), and let \(L=Rh\oplus Re\) be the rank-two solvable Lie ring with \([h,e]=e\). For every integer \(m\ge2\), the number of pairs \((X,Y)\in L^2\) realizing any prescribed \(m\)-fold left Engel value \(\operatorname{ad}_X^m(Y)=te\) is determined explicitly by the valuation of \(t\), through the formulas below. All other targets in \(L\) have empty fibers.

For \(0\le j<\ell\), define \(c_j=(q-1)q^{\ell-j-1}\), and let \(c_\ell=1\). For \(0\le s\le\ell\), the number \(M_s\) of first inputs \(X\) whose linear operator \(\operatorname{ad}_X^m:L\to Re\) has image \(\pi^s Re\) is
\[
M_s=\mathbf 1_{s=0}c_0q^\ell+\mathbf 1_{s=\ell}q^\ell+\sum_{i=1}^{\ell-1}c_i\left(\sum_{j=0}^{i-1}c_j\mathbf 1_{s=\min(\ell,(m-1)i+j)}+q^{\ell-i}\mathbf 1_{s=\min(\ell,mi)}\right).
\]
Here \(\pi\) generates the maximal ideal and \(\mathbf1\) denotes an indicator. For a target \(t\in R\), put \(k=\nu(t)\) where \(\nu(0)=\ell\). The exact prescribed-target fiber size is
\[
\boxed{N_m(t)=\sum_{s=0}^{k}M_sq^{\ell+s}.}
\]
This is a formula for every finite chain ring with the specified \((q,\ell)\), independently of its characteristic or ramification.

More sharply, define the set of nontrivial fiber-jump valuations
\[
H_{m,\ell}=\{1,\ldots,\ell-1\}\cap\bigcup_{i=1}^{\ell-1}\{(m-1)i,(m-1)i+1,\ldots,mi\}.
\]
Then \(N_m(t)\) strictly increases when the target valuation passes \(s\in H_{m,\ell}\), and is constant across every intervening valuation gap. Its full prescribed-target distribution on the line \(Re\), including zero, has exactly \(2+|H_{m,\ell}|\) different fiber sizes. In particular, **all nonzero targets have the same fiber size exactly when \(m\ge\ell+1\)** (for the stipulated \(m\ge2\)). In this stable regime
\[
N_m(t)=\begin{cases}(q-1)q^{3\ell-1},&t\ne0,\\ (q-1)q^{3\ell-1}+q^{4\ell-1},&t=0.\end{cases}
\]

## Assumptions and scope
A finite commutative chain ring has a unique maximal ideal \((\pi)\) whose ideal chain is \(R\supsetneq\pi R\supsetneq\cdots\supsetneq\pi^{\ell-1}R\supsetneq\pi^\ell R=0\). The residue quotient is \(\mathbb F_q\), and \(|\pi^iR|=q^{\ell-i}\). The valuation \(\nu(a)\) is the largest \(i\le\ell\) with \(a\in\pi^iR\). The Lie bracket on \(L\) is alternating and \(R\)-bilinear, with \([h,h]=[e,e]=0\), \([h,e]=e\), and \([e,h]=-e\). The repeated bracket convention is \(\operatorname{ad}_X^m(Y)=[X,[X,\ldots,[X,Y]\ldots]]\), with \(m\) instances of \(X\). It is not a group Engel word map.

The conclusion concerns ordered inputs, a fixed prescribed output, and every \(m\ge2\), \(q\ge2\), \(\ell\ge1\). It does not classify Engel maps for arbitrary Lie rings or non-chain local rings.

## Proof
Write \(X=ah+be\) and \(Y=ch+de\). The first bracket is \([X,Y]=(ad-bc)e\). Since \([X,e]=ae\), induction yields
\[
\operatorname{ad}_X^m(Y)=a^{m-1}(ad-bc)e.
\]
For fixed \((a,b)\), its linear dependence on \((c,d)\) has coefficients \(-a^{m-1}b\) and \(a^m\). Its image ideal is therefore \(a^{m-1}(a,b)R\). If \(a\) is a unit, this is \(R\), and there are \(c_0q^\ell\) such first inputs. If \(a=0\), the image is zero for \(m\ge2\), and there are \(q^\ell\) such first inputs.

Suppose \(\nu(a)=i\) with \(1\le i<\ell\). If \(\nu(b)=j<i\), the image has valuation \(\min(\ell,(m-1)i+j)\). If \(\nu(b)\ge i\), it has valuation \(\min(\ell,mi)\). Exactly \(c_i\) values of \(a\) have valuation \(i\), exactly \(c_j\) values of \(b\) have valuation \(j\), and exactly \(q^{\ell-i}\) values of \(b\) satisfy \(\nu(b)\ge i\). Summation proves the formula for \(M_s\). Necessarily \(\sum_sM_s=|R|^2=q^{2\ell}\).

For an \(X\) in stratum \(s\), the linear map \(L\cong R^2\to\pi^sR\) is surjective onto an image of order \(q^{\ell-s}\). Each target in that image has \(q^{2\ell}/q^{\ell-s}=q^{\ell+s}\) preimages. The image contains \(te\) precisely when \(\nu(t)\ge s\). Summing proves \(N_m(t)\). Targets outside \(Re\) cannot occur. The law uses only lengths and cardinalities of valuation strata, proving ring-independence.

For \(1\le s<\ell\), the formula for \(M_s\) has positive summands precisely when \(s=(m-1)i+j\) for some \(i\ge1\) and \(0\le j\le i\), which is exactly \(s\in H_{m,\ell}\). The increment \(N_m(\nu=s)-N_m(\nu=s-1)=M_sq^{\ell+s}\) is consequently positive exactly on that set. The additional zero-output valuation \(\ell\) always increases the fiber size because \(M_\ell\ge q^\ell>0\), proving the distinct-level count.

If \(m\ge\ell+1\), then every nonunit \(a\) has \(a^{m-1}=0\), while unit \(a\) produces a surjective linear map. Thus all nonzero fibers have common size \(c_0q^{2\ell}=(q-1)q^{3\ell-1}\); the zero fiber additionally gets \(q^{2\ell}\) choices of \(Y\) for each of the \(q^{2\ell-1}\) choices of \((a,b)\) with nonunit \(a\). Conversely, if \(2\le m\le\ell\), the choice \(\nu(a)=1\), \(\nu(b)=0\) yields an image of valuation \(m-1\) with positive multiplicity, hence unequal nonzero fibers. This proves the sharp cutoff.

## Verification
The included checker `engelspectrum_check.py` enumerates the actual iterated brackets over both \(\mathbb Z/p^\ell\mathbb Z\) and \(\mathbb F_p[t]/(t^\ell)\). It checks the predicted count for every target in all tested rings, and independently checks the mass identity \(\sum_{t\in R}N_m(t)=q^{4\ell}\). Tested rings include lengths \(2,3,4\), residue orders \(2,3\), and depths \(2\) through \(5\), with cases where both ring characteristics differ for the same \((q,\ell)\). See `checks.txt` for the actual output.

For example, for \(q=2\), \(\ell=3\), the depth-two fibers at target valuations \(0,1,2,3\) are respectively \(256,384,768,1536\), in both \(\mathbb Z/8\mathbb Z\) and \(\mathbb F_2[t]/(t^3)\). At depth four they are \(256,256,256,2304\).

## Relationship to prior work
Bandman, Gordeev, Kunyavskii and Plotkin studied images and dominance of Engel Lie polynomials on simple/Chevalley Lie algebras over fields, including an explicit general-field restriction, rather than these target-counting laws on the solvable rank-two Lie ring over arbitrary finite chain rings [1]. Klimenko, Kunyavskii, Morita and Plotkin surveyed word maps on groups and Lie algebras, particularly semisimple and Kac–Moody settings, and noted the scarcity of results for base rings [2]. Bandman, Garion and Grunewald treated Engel distributions in finite simple groups \(\operatorname{PSL}_2(q)\), a group-theoretic rather than this Lie-ring setting [3]. The new claim is not surjectivity of an Engel map in a simple group or Lie algebra; it is the full depth-and-valuation fiber law together with the sharp stabilization threshold in finite solvable Lie rings.

## Limitations
The counting formula is elementary once the scalar Engel expression and chain-ring valuations are established. A broader previously published all-word-map counting theorem might imply this specialization without mentioning these coordinates; the searches and inspected sources below did not locate one. Priority is therefore subject to independent bibliographic scrutiny. The theorem does not extend without modification to local rings whose ideals are not linearly ordered. Experimental checks cover finite cases only; the general assertion rests on the displayed proof.

## References
[1] T. Bandman, N. Gordeev, B. Kunyavskii, and E. Plotkin, *Equations in simple Lie algebras*, arXiv:1012.4106, initial public version December 18, 2010, https://arxiv.org/abs/1012.4106.

[2] E. Klimenko, B. Kunyavskii, J. Morita, and E. Plotkin, *Word maps in Kac-Moody setting*, arXiv:1506.01422, initial public version June 3, 2015, https://arxiv.org/abs/1506.01422.

[3] T. Bandman, S. Garion, and F. Grunewald, *On the surjectivity of Engel words on PSL(2,q)*, arXiv:1008.1397, initial public version August 8, 2010, https://arxiv.org/abs/1008.1397.
