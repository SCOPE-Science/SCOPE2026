# Complete dyadic residue fibers of adjacent ordered Bell gaps

## Finding

The ordered Bell (Fubini) numbers count ordered set partitions:
\[
F_n=\sum_{j=0}^n j!\left\{\begin{matrix}n\\j\end{matrix}\right\},\quad n\ge0.
\]
Define the **adjacent gap sequence** \(D_n=F_{n+1}-F_n\). The gap measures how many additional weak orderings arise from adding one labeled element. Indeed, appending the new element as a final singleton block embeds the \(F_n\) ordered partitions among the \(F_{n+1}\) ordered partitions; \(D_n\) counts precisely the remaining arrangements. It is a natural first-difference arithmetic statistic, not the sequence of values \(F_n\) itself.

For each integer \(k\ge7\), set \(P_k=2^{k-6}\) and \(N_k=k-1\). Then, for every integer \(a\ge N_k\), the \(P_k\) gap residues
\[
\{D_n\bmod2^k:a\le n<a+P_k\}
\]
are exactly **one copy each** of the residues \(y\pmod{2^k}\) satisfying \(y\equiv110\) or \(114\pmod{128}\). The least eventual period of the gap sequence modulo \(2^k\) is \(P_k\), and its sharp preperiod is \(N_k\); specifically
\[
\boxed{\nu_2(D_{k-2+P_k}-D_{k-2})=k-1.}
\]
The full residue image, including early indices, is
\[
\boxed{\{0,2,10,62,466,4142\}\cup\{y\bmod2^k:y\equiv110\ \text{or}\ 114\pmod{128}\}.}
\]
These sets are disjoint modulo \(128\) and have total cardinality \(2^{k-6}+6\). Every eventual residue has natural index density \(2^{6-k}\), and all six exceptional residues have density zero. In \(\mathbb Z_2\), the full closure is
\[
\boxed{(110+128\mathbb Z_2)\cup(114+128\mathbb Z_2)\cup\{0,2,10,62,466,4142\},}
\]
which has normalized Haar measure \(1/64\).

## Assumptions and scope

All indices are integers \(n\ge0\); all moduli are \(2^k\) for integers \(k\ge7\). We use \(\nu_2\) for the valuation of a nonzero integer or two-adic number, and \(\mathbb Z_2\) for the two-adic integer ring. The *least eventual period* is the least positive integer shift preserving all sufficiently late terms. The *sharp starting index* is the earliest index from which the least-period congruence holds at all subsequent indices. Natural densities are taken over consecutive nonnegative indices, and Haar measure is normalized to assign \(\mathbb Z_2\) measure one. The gaps, not the Fubini numbers themselves, form the object of the theorem.

## Proof

**Step 1 — A two-adic series and its exact remainder.** The classical exponential generating function
\[
\sum_{n\ge0}F_n\frac{z^n}{n!}=\frac1{2-e^z}
\]
can be expanded coefficientwise in \(\mathbb Q_2\) as
\[
\frac1{2-e^z}=-\sum_{j\ge1}2^{j-1}e^{-jz},
\qquad F_n=(-1)^{n+1}\sum_{j\ge1}2^{j-1}j^n.\tag{1}
\]
For \(\varepsilon\in\{0,1\}\), define a continuous two-adic interpolation of the **odd-base contribution** by
\[
H_\varepsilon(t)=(-1)^{\varepsilon+1}
\sum_{\substack{j\ge1\\j\text{ odd}}}2^{j-1}j^\varepsilon(j^2)^t,
\qquad t\in\mathbb Z_2.\tag{2}
\]
This converges uniformly: odd squares lie in \(1+8\mathbb Z_2\), so \((j^2)^t\) exists for every \(t\in\mathbb Z_2\). For an integer \(n=2t+\varepsilon\), the difference between \(F_n\) and \(H_\varepsilon(t)\) is precisely the even-base contribution. Its \(j=2\) summand has valuation \(n+1\); all even \(j\ge4\) have larger valuations. Thus
\[
\nu_2(F_n-H_{n\bmod2}(\lfloor n/2\rfloor))=n+1.\tag{3}
\]

**Step 2 — Two natural gap branches.** Define
\[
G_0(t)=H_1(t)-H_0(t)
=\sum_{\substack{j\ge1\\j\text{ odd}}}2^{j-1}(j+1)(j^2)^t,\tag{4}
\]
\[
G_1(t)=H_0(t+1)-H_1(t)
=-\sum_{\substack{j\ge1\\j\text{ odd}}}2^{j-1}j(j+1)(j^2)^t.\tag{5}
\]
The errors at consecutive indices have valuations \(n+1\) and \(n+2\), respectively. Consequently the gap has the **exact** interpolation error
\[
\boxed{\nu_2(D_n-G_{n\bmod2}(\lfloor n/2\rfloor))=n+1}\qquad(n\ge0).\tag{6}
\]
Directly evaluating the geometric series at \(t=0\) gives
\[
G_0(0)=\frac29\equiv114\pmod{128},
\qquad G_1(0)=\frac{26}{27}\equiv110\pmod{128}.\tag{7}
\]

**Step 3 — Scaled isometries; the nontrivial additional arithmetic.** For \(u\in1+8\mathbb Z_2\) and distinct \(t,s\in\mathbb Z_2\), the two-adic logarithm gives
\[
\nu_2(u^t-u^s)=\nu_2(u-1)+\nu_2(t-s).\tag{8}
\]
In each of (4) and (5), the \(j=1\) term is constant and drops out of a difference. The \(j=3\) coefficient has valuation \(4\) in **both** branches: \(4(3+1)=16\) and \(-4\cdot3(3+1)=-48\). Since \(\nu_2(9-1)=3\), its contribution to \(G_\varepsilon(t)-G_\varepsilon(s)\) has valuation exactly \(7+\nu_2(t-s)\). For the next odd base \(j=5\), the coefficients \(96\) and \(-480\) have valuation \(5\), and the resulting differences have valuation at least \(8+\nu_2(t-s)\). For all \(j\ge7\) odd, the difference terms have valuation at least \(10+\nu_2(t-s)\). Thus a unique lowest-valuation summand survives and
\[
\boxed{\nu_2(G_\varepsilon(t)-G_\varepsilon(s))=7+\nu_2(t-s)}\quad(t\ne s).\tag{9}
\]
By (7) and (9), each \(G_\varepsilon\) is a scaled isometric bijection of \(\mathbb Z_2\) onto one **entire** ball \(110+128\mathbb Z_2\) or \(114+128\mathbb Z_2\). Indeed, reduction modulo \(2^{m+7}\) is injective on the \(2^m\) arguments modulo \(2^m\), and the target ball also contains exactly \(2^m\) such residues. Compatibility of these finite bijections gives the inverse-limit assertion.

**Step 4 — Complete residue fibers, minimal period, and sharp onset.** Fix \(k\ge7\). If \(n\ge k-1\), (6) yields \(D_n\equiv G_{n\bmod2}(\lfloor n/2\rfloor)\pmod{2^k}\). Every block of \(2^{k-6}\) consecutive indices contains \(2^{k-7}\) consecutive arguments for each parity. Equation (9) makes the two branches bijective over their disjoint balls at modulus \(2^k\), giving one representative of every allowed residue in any such block.

An eventual period \(T\) must be even, because the two branches differ modulo \(128\). Writing \(T=2u\), the branch difference in (9) is \(7+\nu_2(u)=6+\nu_2(T)\), so a period modulo \(2^k\) must be divisible by \(2^{k-6}\). Hence the period just found is minimal.

At \(n=k-2\), the branch difference after the shift \(P_k\) is divisible by \(2^k\). By (6) the interpolation error at the earlier index has valuation exactly \(k-1\), while the error at the later index has higher valuation. Their difference therefore has valuation \(k-1\), proving the displayed sharpness identity and excluding any smaller starting index for the least period or its positive multiples.

**Step 5 — All values and the closure.** The first seven Fubini numbers are \(1,1,3,13,75,541,4683\), giving \(D_0,\ldots,D_5=0,2,10,62,466,4142\). Their reductions modulo \(128\) are distinct and lie outside both balls from (7). For all \(n\ge6\), (6) reduces the gap to the appropriate branch modulo \(128\), since \(n+1\ge7\). Every ball residue at every higher precision appears in the eventual one-per-residue blocks. Thus the full image consists of those two balls and the six exceptional values. Period frequencies give the densities, while inverse limits give the closure. The balls each have Haar measure \(1/128\), and the isolated six points have measure zero, proving the value \(1/64\).

## Verification

The standalone standard-library checker `verify.py` reconstructs the ordered Bell numbers using the binomial recurrence and cross-checks the first 30 rows via the Stirling-number formula. It exhaustively examines the gap distributions for all \(7\le k\le15\), testing 45 whole period blocks, 5,110 residue observations, 6,232 scaled-isometry comparisons, 360 series identities, early exceptional values, sharp preperiods, and least-period assertions. Additional tests compare successive two-adic branch values modulo \(2^{17}\), \(2^{19}\), and \(2^{23}\). Run `python3 verify.py`. Finite tests support, but do not replace, the unrestricted argument.

## Relationship to prior work

Poonen's *Periodicity of a Combinatorial Sequence* (1988), Theorems 4–6, **already establishes the least eventual period of the original Fubini sequence**, \(2^{k-4}\) modulo \(2^k\), and that it is a period from index \(k-1\). These facts are acknowledged as prior results, not claims of novelty. Poonen's one-step shift relation \(F_{n+2^m}-F_n\equiv2^{m+4}\pmod{2^{m+5}}\) is independent of \(n\); subtracting consecutive instances cancels its leading constant. It gives periodicity information for the gap sequence, but **does not imply** the new exact gap value image, its one-per-residue fiber counts, the smaller least gap period, or the two-adic closure. The proof here requires a separate leading-term analysis of the adjacent-difference interpolation functions in (4)–(9).

Barsky had earlier proved broad prime-power periodicity of Fubini numbers (Proposition 1). Mező's 2013 paper describes Gross's decimal last-digit Fubini congruence and extensions to restricted partitions. Asgari and Jahangiri's 2017 paper treats periods of \(r\)-Fubini sequences and cites Poonen's ordinary case, not complete residue fibers for adjacent Fubini differences. OEIS A000670 records the underlying Fubini sequence. General periodicity, the EGF, and the ordinary-sequence least period are all established prior art. The distinguishing new object is the **adjacent gap sequence**, and the new result is its complete modular value distribution at all dyadic scales, together with the exact two-adic closure and onset.

## Limitations

The result is specific to adjacent differences and powers \(2^k\) with \(k\ge7\), not to general gaps or arbitrary primes. A nearby 2017 paper by Diagana and Maïga on other Fubini congruences was located by title and abstract, but a lawful accessible full text was not found; it remains a historical priority risk, though its available abstract does not show the exact adjacent-gap result. An unlocated equivalent theorem may exist, and no independent priority certification or independent audit has been performed. Earlier broad period theorems are not presented as novel.

## References

1. B. Poonen, *Periodicity of a Combinatorial Sequence*, Fibonacci Quarterly 26 (1988), 70–76, https://www.fq.math.ca/Scanned/26-1/poonen.pdf (Theorems 4–6 and references to Good).
2. I. Mező, *Periodicity of the Last Digits of Some Combinatorial Sequences*, arXiv:1308.1637, first posted 2013-08-07, https://arxiv.org/abs/1308.1637; full text https://cs.uwaterloo.ca/journals/JIS/VOL17/Mezo/mezo19.pdf.
3. D. Barsky, *Analyse p-adique et suites classiques de nombres*, original 1982, revised 1995, Proposition 1, https://www.mat.univie.ac.at/~slc/opapers/s05barsky.pdf.
4. A. A. Asgari and M. Jahangiri, *On the Periodicity Problem of Residual r-Fubini Sequences*, arXiv:1701.07276 (2017), https://arxiv.org/abs/1701.07276.
5. T. Diagana and H. Maïga, *Some New Identities and Congruences for Fubini Numbers*, J. Number Theory 173 (2017), 547–569, DOI:10.1016/j.jnt.2016.09.032 (abstract accessed; full primary text not obtained).
6. OEIS A000670, *Fubini numbers*, https://oeis.org/A000670.
