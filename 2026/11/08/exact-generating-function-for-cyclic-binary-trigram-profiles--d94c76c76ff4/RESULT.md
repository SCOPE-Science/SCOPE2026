# Exact generating function for cyclic binary trigram profiles

## Finding
For every integer \(n\geq 1\), let a binary cyclic word be an indexed word \(w=(w_0,\ldots,w_{n-1})\in\{0,1\}^n\), with subscripts interpreted modulo \(n\). Its *trigram profile* records, for each \(u\in\{0,1\}^3\), the number \(m_u(w)=|\{i: (w_i,w_{i+1},w_{i+2})=u\}|\). Let \(P_n\) be the number of different vectors \((m_u(w))_{u\in\{0,1\}^3}\) obtained from any such word.

Then the following equalities hold as formal power series:

\[
\begin{aligned}
\sum_{n\ge1}P_nz^n={}&\frac{2z}{1-z}+\frac{z^2}{1-z^2}\\
&+\frac{2z}{(1-z)^2}\left(\frac{z^2}{1-z^2}-\frac{z^3}{1-z^3}\right)\\
&+\frac{z^2}{(1-z)^4}\left(\frac{1}{1-z^2}-\frac{2}{1-z^3}+\frac{1}{1-z^4}\right)\\
={}&\frac{z(2-3z+z^2-z^3+5z^5-5z^6+6z^7-7z^8+3z^9)}
{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.
\end{aligned}
\]

The first values, for \(n=1,\ldots,16\), are \(2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271\). In particular \(P_n\sim n^4/288\); this leading coefficient was already tabulated in [1] and is not claimed as new. For the noiseless channel transmitting only the complete cyclic trigram profile, \(P_n\) is exactly the largest zero-error codebook cardinality (choose one representative of each distinct profile).

## Assumptions and scope
Words are indexed, but two words with the same profile give a single observation; cyclic rotations of a word necessarily have the same profile. Trigrams wrap around the boundary even at \(n=1,2\); repeated indices are permitted. Counts of all eight *ordered* trigrams are retained, not merely their zero-one composition. No noise, missing reads, or probabilistic model is assumed.

## Proof
Construct the directed binary order-two de Bruijn graph: its vertices are \(00,01,10,11\), and each trigram \(abc\) is an edge from \(ab\) to \(bc\). Traversing a length-\(n\) circular word gives a closed directed walk of length \(n\) with edge multiplicities \(m_{abc}\). Conversely, a nonzero nonnegative integral edge-multiplicity vector arises from a circular word exactly when it has balanced in- and out-degree at every vertex and its nonzero-edge support is connected when edge orientations are forgotten. Indeed, balance and connected nonzero support give an Eulerian circuit, and its edge labels overlap consistently to form the required circular word. This equivalence includes loops and repeated edges and applies at every positive length.

Conservation at vertices \(00\) and \(11\) yields \(m_{001}=m_{100}=:b\) and \(m_{011}=m_{110}=:d\). Conservation at \(01\) yields \(m_{010}+d=b+m_{101}=:t\). Thus every balanced vector has the unique parametrization
\[
(m_{000},m_{001},m_{010},m_{011},m_{100},m_{101},m_{110},m_{111})
=(a,b,t-d,d,b,t-b,d,h),
\]
where \(a,h,t\) are nonnegative integers, \(0\le b,d\le t\), and its total length is \(n=a+h+2t+b+d\).

Connectedness gives exactly four disjoint support regimes:

1. If \(t=0\), only the loops \(000\) and \(111\) can occur. Exactly one loop must have positive multiplicity. Their generating function is \(2z/(1-z)\).
2. If \(t\ge1\) and \(b=d=0\), the two edges \(010\) and \(101\) form a connected two-cycle. Both loop counts must vanish, giving \(z^2/(1-z^2)\).
3. If \(t\ge1\) and exactly one of \(b,d\) is positive, say \(b=j\in\{1,\ldots,t\}\), the loop at the absent fourth vertex must vanish, whereas the loop at the attached vertex can have any multiplicity. There are two symmetric possibilities, yielding
\[
\frac{2}{1-z}\sum_{t\ge1}z^{2t}\sum_{j=1}^t z^j
=\frac{2z}{(1-z)^2}\left(\frac{z^2}{1-z^2}-\frac{z^3}{1-z^3}\right).
\]
4. If \(t\ge1\) and \(b,d\in\{1,\ldots,t\}\), all four vertices lie in one connected component. Both loops are arbitrary, yielding
\[
\frac{1}{(1-z)^2}\sum_{t\ge1}z^{2t}\left(\sum_{j=1}^t z^j\right)^2
=\frac{z^2}{(1-z)^4}\left(\frac{1}{1-z^2}-\frac{2}{1-z^3}+\frac{1}{1-z^4}\right).
\]

The regimes are exhaustive, disjoint, and count each realizable profile exactly once. Summation proves the first generating-function identity. Clearing denominators gives the stated reduced rational form (checked independently by an exact polynomial cross-product program). Since the sole pole of order five on the unit circle is at \(z=1\), and the leading \((1-z)^{-5}\) coefficient is \(1/12\), standard coefficient extraction gives \(P_n\sim (1/12)n^4/24=n^4/288\). The codebook claim follows by one representative per observation, and by the pigeonhole principle no two codewords with the same observation can be distinguished.

## Verification
The included dependency-free programs are executable with Python 3 using `python verify_words.py`, `python verify_flows.py`, and `python verify_identity.py`. `verify_words.py` enumerates all binary indexed words of lengths 1–16 and computes the distinct eight-dimensional profiles directly. `verify_flows.py` independently enumerates all balanced vectors through total length 40, testing connectivity of the nonzero support in the de Bruijn graph. `verify_identity.py` proves the displayed rational identity by exact integer-polynomial cross multiplication. These finite checks reproduce the first coefficients and test the algebra; the all-length theorem rests on the Eulerian argument above, not on extrapolation of the computations.

## Relationship to prior work
Kiah, Puleo and Milenkovic [1] established the general DNA sequence-profile and de Bruijn-flow framework and tabulated the asymptotic coefficient \(c(2,3)=1/288\). That asymptotic value follows also from this exact formula, but is *not* a new observation here. Jacquet, Knessl and Szpankowski [2] developed counting for first-order Markov types (balanced symbol-to-symbol matrices); their formula does not directly provide the connected-support count for eight order-two binary trigram edges. The 2009 higher-order discussion [3] anticipates the replacement of the number of states by higher-order contexts in asymptotic analysis, not this exact rational series. The asserted distinction is the complete finite-length cyclic binary trigram-profile enumeration, with explicit corrections for disconnected balanced supports.

## Limitations
This theorem addresses only binary circular words and ordered windows of length three. It is not an exact enumeration of linear-word profiles, arbitrary alphabet sizes, longer windows, or noisy channels. The full text of a potentially relevant extended 2012 Markov-type paper [4] was not available for inspection, and a small risk of an unindexed equivalent formula remains; no claim of exhaustive historical priority or independent validation is made. The leading asymptotic term is already known from [1].

## References
[1] H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837, original public version dated 2014-10-31; revised as *Codes for DNA Sequence Profiles*. https://arxiv.org/abs/1410.8837

[2] P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, Discrete Mathematics & Theoretical Computer Science (2010). https://dmtcs.episciences.org/en/articles/2768

[3] P. Jacquet, C. Knessl, W. Szpankowski, *Markov Types Again Revisited*, 2009 preprint. https://www.cs.purdue.edu/homes/spa/papers/markov-types.pdf

[4] P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory (2012), DOI: 10.1109/TIT.2012.2191476. https://doi.org/10.1109/TIT.2012.2191476
