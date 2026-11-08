# A square-root law for maximal extinction times in three-state excitation on finite paths

## Finding

Consider synchronous three-state Greenberg–Hastings excitation on the open path \(P_n\), with \(n\ge 1\), resting/excited/refractory states \(0,1,2\), and the usual one-excited-neighbor threshold. For an initial word \(a\in\{0,1,2\}^n\), let \(T(a)\) be the first time the state is identically zero. Then \(T(a)\le n+1\) for every \(a\), and the maximum is attained. Let
\[
E_n=\#\{a\in\{0,1,2\}^n:T(a)=n+1\}.
\]
The *exact* ordinary generating function of the sharp-tail population is
\[
\boxed{\sum_{n\ge1} E_nz^{n-1}=\sqrt{\frac{1+z}{1-3z}}.}
\]
In particular the first values, for lengths \(1,2,\dots,12\), are
\[
1,2,4,10,26,70,192,534,1500,4246,12092,34606.
\]
For independent uniformly chosen initial states,
\[
\boxed{\Pr(T=n+1)=\frac{E_n}{3^n}\sim\frac{2}{3\sqrt{3\pi n}}.}
\]
Thus maximal-duration extinction is only polynomially rare, even though all paths eventually become quiescent. The integer sequence and its generating function as a **combinatorial enumeration** were already known (OEIS A025565); the finding concerns its precise realization as the maximal-extinction shell of this excitation dynamics.

## Assumptions and scope

The path has vertices \(1,\dots,n\), edges between consecutive vertices, and *free*, not periodic, boundary conditions. All updates are simultaneous. Every vertex in state \(1\) changes to \(2\); every vertex in state \(2\) changes to \(0\); a vertex in state \(0\) changes to \(1\) iff at least one path neighbor currently has state \(1\), remaining \(0\) otherwise. Initial configurations are labelled and counted without symmetry reduction. Statements hold for every integer \(n\ge1\), without a probabilistic assumption except for the stated uniform probability.

## Proof

**1. An exact max-plus representation.** Define the indicator \(e_t(v)\) to be one if vertex \(v\) changes from resting to excited on the update from time \(t\) to \(t+1\), and zero otherwise. Associate to an initial coloring \(a\) an integer height \(h_0\) by \(h_0(1)=0\) and
\[
h_0(i+1)-h_0(i)=\mathbf1_{\{a_i=0,a_{i+1}=1\}}-\mathbf1_{\{a_i=1,a_{i+1}=0\}}.
\]
For every time \(t\), set \(h_{t+1}(v)=\max_{u\in N[v]}h_t(u)\), with \(N[v]\) the *closed* path neighborhood. We establish by induction the following exact two identities:
\[
h_t(i+1)-h_t(i)=\mathbf1_{\{X_t(i)=0,X_t(i+1)=1\}}-\mathbf1_{\{X_t(i)=1,X_t(i+1)=0\}},
\qquad h_{t+1}(v)-h_t(v)=e_t(v).
\]
Indeed, for a currently resting vertex \(v\), its neighbor has a larger height exactly when that neighbor is excited, and the excess is then exactly one; for a nonresting vertex, no neighbor has a larger height. Thus the closed-neighborhood maximum increments \(h_t(v)\) precisely by \(e_t(v)\). It remains to verify the displayed gradient at the next step. For any adjacent states, checking the nine ordered pairs gives the gradient-change identity
\[
d(X_{t+1}(i),X_{t+1}(i+1))-d(X_t(i),X_t(i+1))=e_t(i+1)-e_t(i),
\]
where \(d(p,q)=\mathbf1_{\{p=0,q=1\}}-\mathbf1_{\{p=1,q=0\}}\). The only pairs allowing asymmetric external excitations are those with a resting endpoint; inserting its possible excitation gives the identity in either case. Summing the increments proves the induction. Equivalently, this is the familiar excitation-count/height representation for the three-state rule, here derived for free boundary conditions.

Iteration of local maxima on a path yields exactly
\[
h_t(v)=\max_{\lvert i-v\rvert\le t}h_0(i).
\]
The diameter of \(P_n\) is \(D=n-1\); hence \(h_t\) is constant over vertices, and stable in time, for every \(t\ge D\). There are no new excitations after this point. Since excitation \(1\) progresses through refractory \(2\) before returning to \(0\), the entire configuration is zero by \(D+2=n+1\).

**2. Exact characterization of the last extinction layer.** For \(n\ge2\), an excitation occurs on the update from \(D-1\) to \(D\) exactly when some \(h_D(v)>h_{D-1}(v)\). Only the two endpoints can change: all interior vertices already see the complete path at distance \(D-1\). The right endpoint changes precisely when
\[
h_0(1)>\max_{j>1}h_0(j),
\]
and the left endpoint precisely when
\[
h_0(n)>\max_{j<n}h_0(j).
\]
These two *strict endpoint maximum* events cannot occur together. By the three-state refractory delay, the last such excitation is equivalent to first reaching all zero exactly at \(D+2\). Reversal symmetry gives equal counts of the two events. When \(n=1\), only the initially excited state \(1\) needs two updates, giving \(E_1=1\).

**3. Exact boundary-record enumeration.** Count the event \(h_0(n)>h_0(j)\) for all \(j<n\). Read the state word from right to left, and define the running reversed height difference. The increment when the current reversed letter is \(p\) and the next is \(q\) is
\[
\delta(p,q)=\mathbf1_{\{p=1,q=0\}}-\mathbf1_{\{p=0,q=1\}}.
\]
A strict record means that *every* nonempty prefix sum is positive. The first two reversed letters must therefore be \((1,0)\), leaving current letter \(0\) and height one, with \(n-2\) arbitrary allowed steps thereafter. Introduce \(G_j(z,u)\) counting continuations ending in letter \(j\in\{0,1,2\}\), where \(z\) marks their number and \(u^{k-1}\) marks positive height \(k\). Write \(g(z)=[u^0]G_0(z,u)\). Positive-height transitions yield the exact formal-series system
\[
\begin{aligned}
G_0&=1+z(G_0+uG_1+G_2),\\
G_1&=z\bigl((G_0-g)/u+G_1+G_2\bigr),\\
G_2&=z(G_0+G_1+G_2).
\end{aligned}
\]
The forbidden transition from height one with letter zero to letter one is precisely the subtracted \(g\)-term; no other boundary correction is needed. Solving the system yields a kernel
\[
K(z,u)=z^3(u-1)^2+u(3z-1),
\]
and
\[
G_1(z,u)=-\frac{z(2zg-g+uz-z+1)}{K(z,u)}.
\]
The unique *small* formal-series root \(U(z)\) of \(K(z,u)=0\), characterized by \(U(0)=0\), is
\[
U(z)=\frac{1-3z+2z^3-\sqrt{(1-3z)(1-3z+4z^3)}}{2z^3}.
\]
Because \(G_1\) has no negative powers of \(u\), its numerator must vanish at \(u=U(z)\). It follows that
\[
g(z)=\frac{1-z+zU(z)}{1-2z}.
\]
Putting \(S(z)=\sum_jG_j(z,1)\), summing the three equations and substituting \(g\) gives
\[
S(z)=\frac{1-zg(z)}{1-3z}
=\frac{1}{2z}\left(\sqrt{\frac{1+z}{1-3z}}-1\right).
\]
The coefficient \([z^{n-2}]S(z)\) counts one endpoint-record event for \(n\ge2\). Hence \(E_n=2[z^{n-2}]S(z)\), and the special case \(E_1=1\) gives the stated generating function.

**4. Sharp asymptotic.** Near its unique dominant singularity \(z=1/3\), the generating function is asymptotic to \((2/\sqrt3)(1-3z)^{-1/2}\). Therefore
\[
E_n\sim\frac{2}{\sqrt3}\frac{3^{n-1}}{\sqrt{\pi(n-1)}},
\]
which proves the stated probability limit. The positive counts for every \(n\) also prove sharpness of the extinction-time bound.

## Verification

The standalone program `check_exhaustive.py` applies the original simultaneous vertex update to all \(3^n\) labelled states for each \(1\le n\le12\), checks extinction by \(n+1\), checks the strict endpoint-record *if and only if* condition on each word, and checks the coefficients of the square-root series. Its total coverage is \(\sum_{n=1}^{12}3^n=797160\) labelled words. The independent program `check_transfer.py` constructs positive-height meanders by their letter and height and checks the formal-series recurrence through length \(101\). The program `check_maxplus.py` independently checks the excitation-count/maximum representation on all \(9840\) labelled initial words with \(1\le n\le8\), through \(n+3\) updates. Captured outputs are included. All three checks passed. They support, but do not substitute for, the all-length argument above.

## Relationship to prior work

Durrett and Steif (1991) proved an infinite-line one-dimensional decay asymptotic using annihilating excitation waves and random-walk survival. Their infinite-line, two-sided spatial-survival event and asymptotic do not identify the exact maximal *finite free-boundary path* extinction class counted here. Fisch and Gravner (1995) explicitly define free-boundary finite systems and investigate one-dimensional Greenberg–Hastings dynamics, mainly recurrence and fixation regimes; the examined text did not contain this exact sharp-tail enumeration. Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, October 24, 2016) develop the general excitation-count/maximum-height picture and global graph behavior; this work uses that structural perspective while isolating the finite-path extremal layer and computing its entire enumerator.

The coefficients \(E_n\) *already appear* in OEIS A025565, along with the algebraic generating function in other combinatorial guises. Neither the integer sequence, the algebraic square-root function as a formal enumeration, nor the general maximum-height representation is claimed as a novel mathematical object. The claim is the exact identification with the natural longest-extinction class of three-state excitation on a path, including its sharp scaling probability. Existing infinite-line decay results and general finite-graph convergence results do not imply the exact finite path count by themselves.

## Limitations

The theorem applies to open finite paths, three states, synchronous threshold-one Greenberg–Hastings updates, and uniform sampling only for the probability statement. It does not classify all intermediate extinction-time layers, periodic boundaries, larger refractory ranges or other contact thresholds. Historical-priority uncertainty remains because equivalent finite-path extremal results could be unindexed or embedded in broader preexisting analyses, especially older work on one-dimensional excitation and ballot enumeration. No independent audit has been performed.

## References

1. R. Durrett and J. E. Steif, “Some Rigorous Results for the Greenberg–Hastings Model,” *Journal of Theoretical Probability* **4** (1991), 669–690; https://sites.math.duke.edu/~rtd/reprints/paper66.pdf .
2. R. Fisch and J. Gravner, “One-dimensional Deterministic Greenberg–Hastings Models,” *Complex Systems* **9** (1995), 329–348; https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf .
3. J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” arXiv:1610.07320v1, initially posted 2016-10-24; https://arxiv.org/abs/1610.07320v1 .
4. OEIS Foundation, “A025565,” known sequence and generating function; https://oeis.org/A025565 .
