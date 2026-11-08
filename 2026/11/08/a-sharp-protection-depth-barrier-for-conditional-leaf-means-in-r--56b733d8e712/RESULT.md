# A sharp protection-depth barrier for conditional leaf means in random recursive trees

## Finding

Let \(T_n\) be a uniformly random recursive tree on labels \(1,\ldots,n\), rooted at \(1\). Let \(L_n\) be its number of leaves and \(H_n\) the smallest distance from the root to a leaf. For every integer \(h\ge1\) and \(n\ge h+1\), the event \(H_n\ge h\) has positive probability, and the conditional mean satisfies

\[
\mathbb E[L_n\mid H_n\ge h]
=\frac{n-h+1}{2}
\quad\text{if }h\le2\text{ or }n\le h+3,
\]
\[
\mathbb E[L_n\mid H_n\ge h]
<\frac{n-h+1}{2}
\quad\text{if }h\ge3\text{ and }n\ge h+4.
\]

Thus depth three is the first protection threshold at which the linear conditional-leaf identity can fail, and for **each** higher depth the first departure occurs **exactly four vertices beyond the minimal possible order**. The first strict case is \(h=3,n=7\): exactly \(54\) recursive trees satisfy the protection event; their leaf-count distribution has respective counts \(1,31,21,1\) at leaf counts \(1,2,3,4\), and
\[
\mathbb E[L_7\mid H_7\ge3]=\frac{65}{27}<\frac52,
\qquad \frac52-\frac{65}{27}=\frac5{54}.
\]

## Assumptions and scope

A recursive tree on \(n\) vertices is a rooted labeled tree with root label \(1\) and labels strictly increasing along every root-to-vertex path. Each such tree is sampled with probability \(1/(n-1)!\), equivalently by attaching vertex \(j\) uniformly to one of the previous \(j-1\) vertices. A leaf has no children, and distance is measured in edges. The event \(H_n\ge h\) is called root protection of depth \(h\), not protection of every vertex. The theorem concerns all integer depths \(h\ge1\) and all \(n\ge h+1\); no statement is made about impossible conditioning events.

## Proof

**1. Marked increasing-tree series.** Define the bivariate exponential generating series
\[
T_h(z,y)=\sum_{n\ge1}\frac{z^n}{n!}
\sum_{\substack{\tau\text{ recursive}\ n\text{-tree}\\ H(\tau)\ge h}}y^{L(\tau)}.
\]
Here \(T_0\) enumerates all recursive trees. The children of the minimum-labeled root form an unordered set of recursive subtrees. If the root has no children it contributes one leaf; if \(h\ge1\), at least one child must exist and each child must satisfy protection depth \(h-1\). Consequently, as formal power-series identities,
\[
\partial_zT_0=y-1+\exp(T_0),\qquad
\partial_zT_h=\exp(T_{h-1})-1\ (h\ge1),
\]
with \(T_h(0,y)=0\). The differentiation removes the smallest label in the standard increasing-tree labeling construction; no probabilistic independence across overlapping subtrees is assumed.

**2. Ordinary coefficient signatures.** Put
\[
A_h(z)=T_h(z,1),\qquad B_h(z)=\left.\partial_yT_h(z,y)\right|_{y=1}.
\]
For \(h\ge1\),
\[
A_h'=e^{A_{h-1}}-1,\qquad
B_h'=e^{A_{h-1}}B_{h-1}.
\]
The base equation yields
\[
A_0=-\log(1-z),\quad
B_0=z+\frac{z^2}{2(1-z)},\quad
A_1=A_0-z,\quad B_1=\frac{z^2}{2(1-z)}.
\]
For every admissible \((h,n)\), \([z^n]A_h>0\), and coefficient ratios give
\[
\mathbb E[L_n\mid H_n\ge h]
=\frac{[z^n]B_h}{[z^n]A_h}.
\]
Indeed a rooted increasing path witnesses the minimum order \(h+1\), and attaching more vertices below the terminal node witnesses all larger orders.

**3. Coefficientwise deficit.** Introduce
\[
D_h=2B_h-zA_h'+(h-1)A_h.
\]
Since \([z^n]zA_h'=n[z^n]A_h\),
\[
[z^n]D_h=[z^n]A_h\left(2\mathbb E[L_n\mid H_n\ge h]-(n-h+1)\right).
\]
Directly \(D_1=0\). For \(h\ge2\), differentiation of the identities above gives
\[
D_h'=e^{A_{h-1}}D_{h-1}
+(h-2)\left[e^{A_{h-1}}(1-A_{h-1})-1\right].\tag{1}
\]
In particular \(D_2=0\). For any formal series \(X\) with zero constant coefficient,
\[
e^X(1-X)-1=-\sum_{k\ge2}\frac{k-1}{k!}X^k.\tag{2}
\]
For every \(j\ge0\), the series \(A_j\) has strictly positive coefficients at every degree \(n\ge j+1\) and no earlier nonzero coefficients. This follows inductively from \(A_0=-\log(1-z)\) and \(A_j'=e^{A_{j-1}}-1\).

**4. Sharp onset and persistence.** Taking \(h=3\) in (1) and using \(D_2=0\) gives \(D_3'=e^{A_2}(1-A_2)-1\). Since \(A_2\) begins at degree three with all later coefficients strictly positive, (2) says the coefficients of \(D_3'\) vanish through degree five and are strictly negative at every degree six or higher. As \(D_3(0)=0\), the coefficients of \(D_3\) vanish through degree six and are strictly negative at every degree seven or higher.

Suppose for some \(h\ge4\) that \(D_{h-1}\) vanishes below degree \(h+3\) and is strictly negative in all degrees from \(h+3\) onward. Multiplication by \(e^{A_{h-1}}\), which has constant coefficient one and otherwise nonnegative coefficients, preserves that exact first negative degree and the negative sign thereafter. The second term in (1) has nonpositive coefficients by (2) and begins no sooner than degree \(2h\), because \(A_{h-1}\) begins in degree \(h\). Since \(2h>h+3\) for \(h\ge4\), \(D_h'\) begins with a strictly negative coefficient in degree \(h+3\) and all subsequent coefficients are strictly negative. Integration gives the same assertion for \(D_h\) beginning in degree \(h+4\). Induction and the coefficient-ratio identity prove every case of the stated theorem.

## Verification

Run \(`python3 checker.py`\) using standard-library Python. Its exact rational bivariate-series extraction checks all \(1\le h\le10\), \(h+1\le n\le21\); it also verifies the coefficientwise deficits from (1). A second computation enumerates every parent-choice sequence for recursive trees through order nine and compares complete conditional leaf distributions with the generating-function coefficients, independently of the recurrence-based sign argument. The checker passes 531 assertions and verifies the \(54\)-tree boundary case. These finite checks are corroboration, not the proof of the infinite assertion.

## Relationship to prior work

Mahmoud and Ward (2015) study the number of protected **vertices** in random recursive trees and the probability that the root is two-protected, using recursive-tree decompositions and moment recurrences. Their result is not the conditional leaf mean for arbitrary protection depth. Gołębiewski and Klimczak (2019) study the marginal distribution of the **root protection number** using generating functions; their accessible abstract does not report the joint statistic of root depth and total leaves. The latter article's full text was not available during the literature comparison, so implicit coverage is an acknowledged risk. Midence-Ordóñez (2022) and its antecedent results relate rank-one vertices of increasing trees to derangements, offering a classical explanation for a low-depth base case; that case is not claimed as novel independently. The asserted contribution here is the sharp **all-depth conditional leaf-mean sign boundary** at \(n=h+4\) for every \(h\ge3\).

## Limitations

The theorem is for uniformly sampled labeled recursive trees, not plane-oriented or arbitrary simply generated trees. It concerns the conditional first moment and gives no conditional distribution formula for arbitrary depth. A general increasing-tree bivariate marking scheme might imply the result indirectly; exhaustive historical priority has not been established. The direct prior-work comparison of the 2019 protection-number paper was limited to accessible abstract and bibliographic material because its full text could not be obtained. No independent audit has been performed.

## References

- H. M. Mahmoud and M. D. Ward, “Asymptotic properties of protected nodes in random recursive trees,” *Journal of Applied Probability* **52** (2015), 290–297. DOI: https://doi.org/10.1239/jap/1429282623 . Lawful author-hosted full text: https://the-examples-book.com/personal/mdw/_attachments/paper029.pdf .
- Z. Gołębiewski and M. Klimczak, “Protection Number of Recursive Trees,” *ANALCO 2019*, 45–53. DOI: https://doi.org/10.1137/1.9781611975505.5 .
- M. Midence-Ordóñez, “A bijection between vertices of rank 1 in increasing trees and derangements,” arXiv:2210.05016 (2022), https://arxiv.org/abs/2210.05016 .
- F. Bergeron, P. Flajolet and B. Salvy, “Varieties of increasing trees,” *Lecture Notes in Computer Science* **581** (1992), 24–48.
