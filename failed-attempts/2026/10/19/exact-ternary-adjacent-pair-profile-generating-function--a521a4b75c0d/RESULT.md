# Exact ternary adjacent-pair profile generating function

## Finding
For a word \(w=w_1\cdots w_n\) over the alphabet \(\{0,1,2\}\), define its adjacent-pair profile by
\[
 C(w)=(c_{ab}(w))_{a,b\in\{0,1,2\}},\qquad
 c_{ab}(w)=\#\{1\le i<n:(w_i,w_{i+1})=(a,b)\}.
\]
Let \(P_3(n)=\#\{C(w):w\in\{0,1,2\}^n\}\). For every \(n\ge1\), the ordinary generating function of the **distinct realizable linear profiles** is exactly
\[
\boxed{\begin{aligned}
\sum_{n\ge1}P_3(n)z^{n-1}
={}&\frac{1+6z+6z^2+z^3}{(1-z)^3(1-z^2)^3(1-z^3)}
-\frac1{(1-z)^3}+1+\frac{3z}{1-z}\\
&-\frac{3z^3+6z^2}{(1-z)^3(1-z^2)}.
\end{aligned}}
\]
Equivalently, this is the single rational function
\[
\frac{1+5z-8z^2+8z^3+13z^4-4z^5-10z^6-8z^7+11z^8+2z^9-5z^{10}+2z^{11}}{(1-z)^7(1+z)^2(1+z+z^2)}.
\]
The first values for word lengths \(1\) through \(13\) are
\[
1,9,24,65,156,342,683,1272,2226,3708,5919,9120,13625.
\]
In particular,
\[
\boxed{P_3(n)=\frac7{8640}n^6+O(n^5)\qquad(n\to\infty).}
\]
The maximum size of a length-\(n\) ternary code whose codewords have pairwise different full adjacent-pair profiles is consequently exactly \(P_3(n)\).

## Assumptions and scope
The alphabet has exactly three distinguishable letters. All \(n-1\) consecutive pairs of a **linear** word are observed with multiplicity and with directed order; the wraparound pair is not observed. A profile is a nine-entry nonnegative integer matrix. Different words can share a profile, and they are counted only once. At \(n=1\) there are no pairs, so all one-symbol words share the zero profile, contributing \(P_3(1)=1\).

All generating functions are ordinary, formal power series in \(z\). Each directed edge occurrence has weight \(z\), so the coefficient of \(z^{n-1}\) counts length-\(n\) word profiles. The coding statement concerns error-free complete pair multispectra, not corrupted or missing reads.

## Proof
**1. Flow and realizability.** Interpret the entry \(c_{ab}\) as the multiplicity of the directed edge \(a\to b\) on the complete digraph with loops on three labeled vertices. If the word begins at \(s\) and ends at \(t\), then its row-minus-column degree imbalance is zero when \(s=t\), and is \(\mathbf e_s-\mathbf e_t\) when \(s\ne t\). Conversely, the directed Euler-trail criterion says that a nonzero edge multiset with either imbalance and **weakly connected positive-degree support** admits a trail traversing every edge exactly once. Its vertex sequence realizes precisely the matrix. The zero matrix represents the length-one profile once. Thus the problem is to count nonnegative matrices in seven disjoint imbalance sectors, removing disconnected edge supports.

**2. All balanced matrices.** Write the three clockwise off-diagonal counts \(c_{01},c_{12},c_{20}\) and the three opposite counts \(c_{10},c_{21},c_{02}\). Zero imbalance forces
\[
c_{01}-c_{10}=c_{12}-c_{21}=c_{20}-c_{02}=h\in\mathbb Z.
\]
For \(h=0\), the three opposite edge pairs independently contribute \((1-z^2)^{-3}\). For positive or negative \(h\), there are additionally three edges per unit of \(|h|\), yielding the factor \(1+2\sum_{h\ge1}z^{3h}=(1+z^3)/(1-z^3)\). The three diagonal loop counts contribute \((1-z)^{-3}\). Hence all nonnegative balanced matrices, **including disconnected ones**, have generating function
\[
B(z)=\frac{1+z^3}{(1-z)^3(1-z^2)^3(1-z^3)}.
\]

**3. All matrices with a specified endpoint imbalance.** Fix distinct endpoints \(s,t\) and ask for imbalance \(\mathbf e_s-\mathbf e_t\). Adding one edge \(t\to s\) produces a balanced matrix with that edge count positive. Conversely, remove one such edge. After dividing by its weight \(z\), this is a bijection between the two sets of matrices. Forbidding one specified reverse off-diagonal edge in a balanced matrix forces the directed-cycle difference to be nonnegative, with the corresponding opposite-edge pair multiplicity zero. Thus the forbidden-edge balanced generating function is
\[
B_0(z)=\frac1{(1-z)^3(1-z^2)^2(1-z^3)}.
\]
Consequently every one of the six nonzero endpoint-imbalance sectors has formal series
\[
A(z)=\frac{B(z)-B_0(z)}z
=\frac{z+z^2}{(1-z)^3(1-z^2)^3(1-z^3)}.
\]
The quotient is a formal power series because the numerator has zero constant term.

**4. Remove every disconnected support.** With zero imbalance, no off-diagonal edge means only loops. Among these, the matrices with loops at two or three vertices are disconnected and have generating series
\[
\frac1{(1-z)^3}-1-\frac{3z}{1-z}.
\]
If at least one off-diagonal edge occurs in a disconnected balanced matrix, it must join exactly two vertices. Their two directed counts must be equal and positive; the third vertex has a positive loop, and loops on the pair are arbitrary. The corresponding generating series, summed over the three vertex pairs, is
\[
\frac{3z^3}{(1-z)^3(1-z^2)}.
\]
These are the only cases: a balanced support on three vertices with off-diagonal connections spanning all three is weakly connected.

For a fixed nonzero imbalance from \(s\) to \(t\), a disconnected support must consist of the connected two-vertex component containing \(s,t\), plus a positive loop at the isolated third vertex. There must be one more edge \(s\to t\) than \(t\to s\); loops on all three vertices are arbitrary. Therefore its generating series is
\[
\frac{z^2}{(1-z)^3(1-z^2)}.
\]
There are six disjoint endpoint sectors, so subtract six copies. No other disconnection is possible on a three-letter alphabet with these imbalances.

Combining the balanced sector, the six nonzero sectors and all disconnection corrections gives
\[
B(z)+6A(z)-\left(\frac1{(1-z)^3}-1-\frac{3z}{1-z}\right)
-\frac{3z^3+6z^2}{(1-z)^3(1-z^2)},
\]
which simplifies to the claimed rational expressions.

**5. Leading term and code capacity.** As \(z\to1\), the coefficient of \((1-z)^{-7}\) in \(B(z)\) is \(1/12\), and that in each \(A(z)\) is \(1/12\). All disconnection corrections have poles of order at most four. Therefore the total leading pole coefficient is \(7/12\). The other poles of the reduced rational function are roots of unity of order two or three, so partial fractions yield a degree-six quasipolynomial in \(n\) with leading coefficient \((7/12)/6!=7/8640\), and an error \(O(n^5)\). Finally, a profile-distinguishable code has at most one representative of each profile; selecting one realizing word per profile attains \(P_3(n)\). This proves the statements for every \(n\ge1\).

## Verification
The standalone `verify.py` uses only the Python standard library. It independently enumerates all ternary words through length \(9\), enumerates all nine-entry nonnegative matrices of total edge count at most \(12\) and decides Euler-trail realizability directly, constructs the claimed rational generating series from binomial-series arithmetic, checks both routes against its coefficients, and verifies the reduced rational identity. Running `python3 verify.py` prints `VERIFY_OK` if every assertion passes. The resulting finite values for \(n\le13\) are stated above. These finite checks corroborate, but do not replace, the proof of the infinite formula.

## Relationship to prior work
Jacquet, Knessl, and Szpankowski's *Counting Markov Types* (2010) develops balanced-matrix enumeration and gives the exact ternary generating function for **balanced** frequency matrices (cyclic closure), with its leading coefficient. The present formula counts **linear** string profiles with arbitrary endpoints. Its six nonbalanced sectors and its exact weak-connectivity corrections change all coefficients and multiply the degree-six leading term by seven. The 2012 expanded IEEE article has a closely relevant title and balanced-matrix abstract; its full text was not available for comparison, so implicit earlier coverage there remains a literature risk.

Kiah, Puleo, and Milenkovic's *Codes for DNA Sequence Profiles* (2015), Section 3 and Theorem 3.5, addresses precisely this general profile model and quotes the asymptotic factor \(q^2-q+1\) for pair profiles relative to cyclic types, but does not state the all-length ternary rational function above. Chang and collaborators' *Rates of DNA Sequence Profiles for Practical Values of Read Lengths* (2016) gives general asymptotics and a formula in a short-length regime only, not an all-length ternary enumeration. A published exact **binary** pair-multispectrum calculation does not imply this ternary formula, because its graph has only two vertices and none of the three-cycle or third-vertex disconnection corrections.

## Limitations
The formula applies only to the ternary alphabet and complete error-free adjacent-pair multispectra of linear words. It does not count cyclic profiles, longer reads, partial observations, or profile class multiplicities. The construction attaining the optimal code size chooses arbitrary representatives and does not supply a ranking or efficient encoder. The literature comparison is limited by lack of full access to the expanded 2012 IEEE article and the possibility of an unindexed equivalent enumeration. The finite checks are not an independent audit of the proof.

## References
1. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768. Public source: https://dmtcs.episciences.org/2768 ; full text: https://dmtcs.episciences.org/en/articles/2768/download .
2. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58 (2012), 4261–4272, DOI:10.1109/TIT.2012.2191476 (abstract available; full text not inspected).
3. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1, 2 February 2015, https://arxiv.org/pdf/1502.00517 .
4. C.-H. Chang et al., *Rates of DNA Sequence Profiles for Practical Values of Read Lengths*, arXiv:1607.02279v1, 8 July 2016, https://arxiv.org/pdf/1607.02279 .
5. Published *Exact binary two-multispectrum code size and singleton classification*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71 (binary-only comparison).
