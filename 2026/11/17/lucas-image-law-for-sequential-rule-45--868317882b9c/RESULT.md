# Lucas image law for sequential Rule 45

## Finding

Let \(n\ge3\), and let \(S_n:\{0,1\}^n\to\{0,1\}^n\) be one complete left-to-right sequential sweep, in the order \(0,1,\ldots,n-1\), of elementary cellular automaton Rule \(45\) on a labelled cyclic ring. Let \(I_n\) be its set of distinct one-sweep outputs.

For any output candidate \(y=(y_0,\ldots,y_{n-1})\), put
\[
 m_i(y)=\mathbf 1_{\{y_i=y_{i-1}\}}\quad(1\le i\le n-2),\qquad
 q(y)=y_{n-1}\oplus y_{n-2}.
\]
Then \(y\in I_n\) **if and only if** all of the following hold:

1. \(m_im_{i+1}=0\) for each \(1\le i\le n-3\).
2. If \(y_0=0\), then \(q=1\).
3. If \(y_0=1\) and \(q=0\), then \(m_{n-2}=0\); if \(y_0=1\) and \(q=1\), then \(m_1=0\).

The number of distinct reachable outputs is exactly
\[
 \boxed{|I_n|=L_n=F_{n-1}+F_{n+1}=\varphi^n+(-\varphi^{-1})^n},
\]
where \(F_0=0\), \(F_1=1\), \(F_{r+2}=F_{r+1}+F_r\), and \(\varphi=(1+\sqrt5)/2\). Thus the number of one-step Garden-of-Eden configurations is \(2^n-L_n\), the image entropy per cell is \(\log\varphi\), and the reachable proportion \(L_n/2^n\) decays exponentially.

## Assumptions and scope

The local Rule \(45\) map takes its three **current** inputs (left, center, right) and returns
\[
 f(a,b,c)=a\oplus(b\lor\neg c).
\]
The three inputs at vertex \(i\) are indexed cyclically modulo \(n\), and its state is replaced immediately before vertex \(i+1\) is processed. This is one sequential sweep, not one synchronous Rule \(45\) update. Labels and the starting vertex are fixed; spatial rotations are distinct configurations. The theorem holds for all integer \(n\ge3\), whether or not \(3\mid n\). A reachable output need not be recurrent or fixed.

## Proof

Write \(x=(x_0,\ldots,x_{n-1})\) for a preimage and \(y=S_n(x)\). At vertex \(0\), the left neighbor still has its old value \(x_{n-1}\), hence
\[
 y_0=x_{n-1}\oplus(x_0\lor\neg x_1). \tag{1}
\]
For \(1\le i\le n-2\), the left neighbor has already changed to \(y_{i-1}\) while the right neighbor has not changed, giving
\[
 y_i=y_{i-1}\oplus(x_i\lor\neg x_{i+1}). \tag{2}
\]
At the final vertex the right neighbor has already changed to \(y_0\), so
\[
 q=y_{n-1}\oplus y_{n-2}=x_{n-1}\lor\neg y_0. \tag{3}
\]
Equation (2) says that \(m_i=1\) **exactly when** \((x_i,x_{i+1})=(0,1)\); two consecutive \(m_i\)'s therefore cannot both equal one. Equation (3) implies \(q=1\) if \(y_0=0\), and \(q=x_{n-1}\) if \(y_0=1\). If \(y_0=1,q=0\), the last mark must be zero, since a last mark would force \(x_{n-1}=1\). If \(y_0=1,q=1\), (1) forces \((x_0,x_1)=(0,1)\), so the first mark must be zero, since a first mark would force \(x_1=0\). This proves necessity.

For sufficiency, take any nonadjacent-mark word \(m_1\ldots m_{n-2}\). Construct binary \(x_1,\ldots,x_{n-1}\) such that \((x_i,x_{i+1})=(0,1)\) precisely at the marked positions and never at an unmarked position. It suffices to use constant zeros before the first marked edge, descend from ones to zeros once between successive marked edges, and use constant ones after the last marked edge; if there are no marks, use a constant word. Because marked edges do not touch, each intervening descent can be placed on an unmarked edge. The same construction permits a prescribed initial one when the first mark is zero (place a descent before the first mark), and permits a prescribed final zero when the last mark is zero (place a descent after the last mark). These prescriptions can be satisfied simultaneously when needed, although the three cases below require at most one of them.

If \(y_0=0\), choose \(x_{n-1}=1,x_0=1\) and a mark-realizing interior word ending in one. Equation (1) gives \(y_0=0\), and (3) gives \(q=1\). If \(y_0=1,q=0\), choose \(x_{n-1}=0,x_0=1\) and a mark-realizing interior word ending in zero; this is possible precisely when the last mark is zero. If \(y_0=1,q=1\), choose \(x_{n-1}=1,x_0=0,x_1=1\) and a mark-realizing interior word starting and ending in one; the first mark must be zero and the right tail can be all ones. Equations (1)--(3) then recover the candidate \(y\), proving sufficiency.

For the count, let \(A_r\) be the number of binary words of length \(r\) with no adjacent ones. The initial values \(A_0=1,A_1=2\) and first-bit decomposition give \(A_r=A_{r-1}+A_{r-2}=F_{r+2}\). The map
\[
 y\longmapsto(y_0,m_1,\ldots,m_{n-2},q)
\]
is bijective: knowing \(y_0\), every mark specifies whether the next bit repeats or flips, and \(q\) specifies the last bit. For \(y_0=0\) there are \(A_{n-2}=F_n\) legal mark words and only \(q=1\). For \(y_0=1,q=0\), the last mark must be zero, leaving \(A_{n-3}=F_{n-1}\) choices; for \(y_0=1,q=1\), the first mark must be zero, again leaving \(F_{n-1}\) choices. Thus \(|I_n|=F_n+2F_{n-1}=F_{n+1}+F_{n-1}=L_n\). The stated asymptotics follow from Binet's formula for \(L_n\).

## Verification

The complete proof applies to all \(n\ge3\). In addition, `check_direct.cpp` directly enumerates all \(2^n\) binary inputs and verifies the predicted image language and Lucas count independently for every \(3\le n\le20\), including the boundary convention of the sequential sweep. Its recorded output is `check_direct.out`; compile with `g++ -std=c++17 -O2 check_direct.cpp -o check_direct` and run `./check_direct`.

The separate Python implementation `check_constructive.py` checks direct outputs against the closed characterization through \(n=15\), and also checks an independently formulated existential preimage solver for every candidate output through \(n=11\). Run with `python3 check_constructive.py`; its recorded output is `check_constructive.out`. These finite checks test implementation and boundary cases but are **not** substitutes for the all-\(n\) argument above.

Examples: \(|I_3|=4\), \(|I_6|=18\), \(|I_9|=76\), \(|I_{12}|=322\), \(|I_{20}|=15127\).

## Relationship to prior work

Macauley, McCammond and Mortveit studied dependence of asynchronous elementary cellular automata on update orders and classified order-independent periodic-state behavior. Goles, Montalva-Medel, Mortveit and Ramirez-Flandes studied block invariance of periodic states. These concern recurrent-state invariance, not the set of all one-sweep outputs for a fixed update order.

Donoso-Leiva, Goles, Ríos-Wilson and Sené studied sequential convergence and explicitly posed the fixed left-to-right Rule \(45\) convergence conjecture at ring lengths divisible by three. Their Rule \(45\) analysis addresses fixed points and convergence, not the image language or its cardinality. The present result is a structural one-sweep information-loss theorem, and **does not prove that conjecture**. Other published elementary-automaton image counts for synchronous rules use different maps; such results cannot imply the sequential Rule \(45\) classification by parameter substitution.

## Limitations

This theorem gives the complete one-sweep image, not its inverse-fiber multiplicities, convergence time, recurrent dynamics, or behavior under other update orders. The spatial entropy refers to cardinality of one-sweep output sets, not to the invariant measure or temporal entropy of the iterated map. A literature search and comparisons with accessible primary texts did not establish an earlier equivalent theorem, but absence from indexed sources does not certify historical priority. Independent external mathematical validation has not been performed.

## References

1. M. Macauley, J. McCammond and H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360, first posted 2007-07-16. https://arxiv.org/abs/0707.2360
2. E. Goles, M. Montalva-Medel, H. S. Mortveit and S. Ramirez-Flandes, *Block Invariance in Elementary Cellular Automata*, Journal of Cellular Automata 10(1–2), 119–135 (2015). https://www.oldcitypublishing.com/journals/jca-home/jca-issue-contents/jca-volume-10-number-1-2-2015/jca-10-1-2-p-119-135/
3. I. Donoso-Leiva, E. Goles, M. Ríos-Wilson and S. Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797, first posted 2025-09-09, especially the Rule 45 section and Conjecture 1. https://arxiv.org/abs/2509.07797
