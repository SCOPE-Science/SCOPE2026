# Exact 3-Abelian reconstruction fibers of the binary golden-mean language

## Finding
Let \(\mathcal G_n\) be the binary length-\(n\) words with no factor `11`. Two words are **3-Abelian equivalent** when, for each binary contiguous factor of length one, two, or three, its number of overlapping occurrences is the same in both words. For \(n\ge0\), let \(C_n\) count the equivalence classes in \(\mathcal G_n\), and let \(U_n\) count classes containing a single word.

**Exact inverse fibers.** Every nonzero-containing word has the unique representation
\[
w=0^{a_0}1\,0^{a_1}1\cdots1\,0^{a_m},\qquad m\ge1,
\]
with \(a_0,a_m\ge0\) and \(a_i\ge1\) for \(1\le i<m\). Put
\[
u=\min(a_0,2),\quad v=\min(a_m,2),\quad
c=|\{1\le i<m:a_i\ge2\}|,\quad
h=\sum_{i=0}^{m}\max(a_i-2,0),\quad
r=c+\mathbf1_{u=2}+\mathbf1_{v=2}.
\]
Two such words are 3-Abelian equivalent **if and only if** their parameter tuples \((m,c,u,v,h)\) agree. All tuples with \(0\le c\le m-1\), \(u,v\in\{0,1,2\}\), and \(h\ge0\) are realized except that \(r=0\) requires \(h=0\). The corresponding fiber contains exactly
\[
\boxed{\binom{m-1}{c}\binom{h+r-1}{r-1}\quad (r\ge1),}
\]
while for \(r=0,h=0\) the fiber is a singleton. Its word length is \(n=2m-1+c+u+v+h\). The all-zero word contributes one additional singleton class at every length. In particular, a nonzero-containing word is uniquely reconstructible precisely when
\[
\boxed{(c=0\ \text{or}\ c=m-1)\quad\text{and}\quad(h=0\ \text{or}\ r=1).}
\]

**Exact profile capacity and singleton count.** The generating functions are
\[
\boxed{\sum_{n\ge0}C_nz^n=\frac{1-z^2+z^3+z^4+z^5}{(1-z)^3(1+z)},}
\qquad
\boxed{\sum_{n\ge0}U_nz^n=\frac{1+z+z^3+2z^4+3z^5+z^6-z^7-3z^8-z^9}{(1-z)^2(1+z)}.}
\]
Consequently, for \(n=2j\ge2\), \(C_n=3j^2-4j+4\); for \(n=2j+1\ge3\), \(C_n=3j^2-j+3\), with \(C_0=1,C_1=2\). The initial singleton values are
\[
(U_0,U_1,\ldots,U_6)=(1,2,3,5,8,13,17),
\]
and for every \(n\ge7\), \(U_n=2n+6\) when \(n\) is even and \(U_n=2n+7\) when \(n\) is odd.

The first ambiguous length is six: the only two nonsingleton classes are \(\{\mathtt{000100},\mathtt{001000}\}\) and \(\{\mathtt{100101},\mathtt{101001}\}\). Under noiseless observation of the complete 3-Abelian profile, the maximum zero-error code size in \(\mathcal G_n\) is exactly \(C_n\). Although \(|\mathcal G_n|\) grows as the Fibonacci numbers, \(C_n=3n^2/4+O(n)\) and \(U_n=2n+O(1)\).

## Assumptions and scope
The alphabet is labeled `0`,`1`; only **linear** words without `11` are considered. Occurrences overlap and are multiplicity-preserving. The observation comprises all one-, two- and three-gram counts (equivalently, for \(n\ge2\), all ordered three-gram counts plus the first and last two symbols). The observation is stronger than an endpoint-free three-gram read multiset. Lengths zero, one and two are handled by their shorter-factor observations. No circular or noisy reconstruction statement is made.

## Proof
**1. Class parameters and recoverability.** All words in \(\mathcal G_n\) with at least one `1` have the displayed zero-run decomposition. For \(n\ge3\), the 3-Abelian observation determines the number \(m\) of ones from its length-one counts and the first and last two symbols from the standard telescoping relation between consecutive factor-count vectors. The first two symbols determine \(u\): `10` means \(u=0\), `01` means \(u=1\), and `00` means \(u=2\). Similarly, suffixes `01`,`10`,`00` give \(v=0,1,2\). Every interior zero gap of length one produces one occurrence of `101`; no other zero gap produces such an occurrence, hence \(c=m-1-N_{101}\). Exactly the excess beyond two zeros in each zero run contributes to `000`, so \(h=N_{000}\).

Conversely, the parameter tuple fixes the five potentially nonzero three-gram multiplicities:
\[
N_{000}=h,\quad N_{001}=c+\mathbf1_{u=2},\quad
N_{100}=c+\mathbf1_{v=2},\quad N_{101}=m-1-c,\quad
N_{010}=m-\mathbf1_{u=0}-\mathbf1_{v=0}.
\]
The other three triple counts are zero. Together with the prefix and suffix two-grams these numbers determine all shorter-factor counts, so they determine the 3-Abelian class. The small cases \(n\le2\) have distinct observations for distinct words and conform to the same tuple classes. The word consisting solely of zeros is separate, since its count of ones vanishes.

**2. Exact fiber cardinality.** Among \(m-1\) interior zero gaps choose which \(c\) have length at least two: \(\binom{m-1}{c}\) choices. Every other interior gap has length one. The \(r\) chosen interior long gaps and long boundary gaps start at exactly two zeros. The boundary categories zero or one are fixed, and their lengths are exactly their category. The nonnegative excess \(h\) is distributed among precisely these \(r\) long gaps. For \(r\ge1\), weak compositions give \(\binom{h+r-1}{r-1}\) choices; for \(r=0\), necessarily \(h=0\). This is a bijection, not an estimate or a finite enumeration. It also proves the length identity and every stated feasibility condition.

The first binomial factor equals one exactly when \(c=0\) or \(c=m-1\). For \(r\ge1\), the second equals one exactly when \(h=0\) or \(r=1\); when \(r=0\) the feasibility rule forces \(h=0\). This gives the singleton condition without any exceptional asymptotic argument.

**3. All profile classes.** Put \(A(z)=(1+z+z^2)^2\), \(B(z)=(1+z)^2\). The sum of base weights of possible interior-gap configurations is
\[
T(z)=\sum_{m\ge1}\sum_{c=0}^{m-1}z^{2m-1+c}
=\frac{z}{1-z}\left(\frac1{1-z^2}-\frac{z}{1-z^3}\right).
\]
Allowing arbitrary \(h\ge0\) initially supplies \(A(z)T(z)/(1-z)\). The terms with \(r=0\) are exactly \(c=0\) and \(u,v\in\{0,1\}\); removing their forbidden positive excess subtracts \(\frac{z}{1-z}\frac{z B(z)}{1-z^2}\). Adding the all-zero word at each length yields
\[
\sum C_nz^n=\frac1{1-z}+\frac{A(z)T(z)}{1-z}-\frac{z^2B(z)}{(1-z)(1-z^2)}
=\frac{1-z^2+z^3+z^4+z^5}{(1-z)^3(1+z)}.
\]

**4. Singleton classes.** Write
\[
B_0(z)=(1+z)^2+\frac{2z^2(1+z)}{1-z}+z^4,
\qquad
B_1(z)=\frac{(1+z)^2}{1-z}+A(z)-(1+z)^2.
\]
For \(c=0\), all \(m\ge1\) have base factor \(z^{2m-1}\); the boundary sum is \(B_0(z)\), since arbitrary surplus is possible precisely when exactly one boundary gap is long. For \(c=m-1\), exclude \(m=1\), already counted. At \(m=2\), the single interior gap is long and surplus is free precisely when both boundary gaps are short, giving \(z^4B_1(z)\). At \(m\ge3\), there are at least two long gaps, so no positive surplus is allowed; the sum is \(z^7A(z)/(1-z^3)\). Consequently
\[
\sum U_nz^n=\frac1{1-z}+\frac{zB_0(z)}{1-z^2}+z^4B_1(z)+\frac{z^7A(z)}{1-z^3}.
\]
Expanding and canceling gives the displayed rational generating function. Elementary partial fractions or comparison of coefficients with \((1-z)^2(1+z)\) yields its explicit eventual parity formulas. The formula for \(C_n\) follows analogously. Direct factor enumeration shows the first two ambiguous pairs at length six and the singleton equality for every smaller length; alternatively, this follows from the binomial formula.

## Verification
The accompanying independent Python programs `verify_direct.py` and `verify_series.py` use only the standard library. `verify_direct.py` groups actual admissible words by every length-one, -two and -three factor count through length 23, and compares all groups with the predicted parameter fibers and exact class/singleton counts; it reports `VERIFY_DIRECT_OK`. `verify_series.py` independently constructs the rational coefficients using integer polynomial recurrences, counts all parameter tuples and their predicted fiber multiplicities through length 130, and checks that summing fiber cardinalities recovers the Fibonacci number of admissible words; it reports `VERIFY_SERIES_OK`. The checks are finite corroboration: the universal proof is the explicit bijection and formal generating-function sums above.

## Relationship to prior work
Karhumäki, Puzynina, Rao and Whiteland (2016) characterize general \(k\)-Abelian equivalence via switchings and prove polynomial upper bounds for singleton classes. Their general theorem does not tabulate this forbidden-`11`, order-three, linear reconstruction spectrum or its exact singleton/quadratic laws. Kiah, Puleo and Milenkovic (2015) set out the multiplicity-preserving read-profile model and constrained de Bruijn counting by Ehrhart theory; their treatment does not supply the exact linear golden-mean fiber formula here.

Closer published exact-profile enumerations include *Exact binary three-gram profile counts under a two-run constraint* (which forbids **both** `000` and `111` and counts three-gram profiles without prefix/suffix information), *Exact finite-length capacity of the linear binary three-gram spectrum* (unrestricted binary words and endpoint-free three-gram observations), and *Exact fibers and uniquely reconstructible profiles for cyclic four-gram reads under a binary run-length constraint* (circular necklaces and four-gram observations). None gives the claimed complete linear 3-Abelian fiber law on words avoiding `11`. General equivalence/fiber methods are acknowledged as prior; the explicit constrained support, complete binomial fiber spectrum and exact two rational counting series are the specialized conclusions here.

## Limitations
No claim is made about the optimal code size under missing reads, substitutions, deletions or an endpoint-free three-gram observation. The asymptotic rate is zero for this fixed-length observation. All counts concern exactly the stated binary source and order-three, linear, complete profile. Published general theorems may permit alternative derivations of special cases; unindexed exact constrained enumerations are an originality risk. No independent external mathematical audit or publication priority determination is claimed.

## References
1. J. Karhumäki, S. Puzynina, M. Rao and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319 (first public May 11, 2016), https://arxiv.org/abs/1605.03319 .
2. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837 (first public October 31, 2014), https://arxiv.org/abs/1410.8837 ; expanded *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (February 2, 2015), https://arxiv.org/html/1502.00517v1 .
3. *Exact binary three-gram profile counts under a two-run constraint*, publicly indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-binary-three-gram-profile-counts-under-a-two-run-constrain--db3743cca7ea .
4. *Exact finite-length capacity of the linear binary three-gram spectrum*, publicly indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-finite-length-capacity-of-the-linear-binary-three-gram-spe--bcc1ebef8280 .
5. *Exact fibers and uniquely reconstructible profiles for cyclic four-gram reads under a binary run-length constraint*, publicly indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fibers-and-uniquely-reconstructible-profiles-for-cyclic-fo--d7a18695ef7b .
