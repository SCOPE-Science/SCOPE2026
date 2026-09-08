"""Dehornoy order comparison via (-1,2)-action? Use Lawrence-Krammer-free approach:
Compare braids x,y by sign of x^{-1}y using Dehornoy's handle-reduction-free
criterion on 3-4 strands via the faithful Artin action on free group + reduced-word
comparison (Dehornoy order = compare images of x_n? ). Simpler rigorous method for
short words: use the characterization via sigma-positive words and the WORD PROBLEM
solved by our Garside for the monoid plus free-group action for inverses.

Approach: to decide sign of word w (with inverses) in B_n: compute its action on
free group F_n generators (Artin representation, faithful). Then w=1 iff action trivial.
To decide Dehornoy positivity: w is sigma-positive iff ... use the effective procedure:
repeatedly apply free reduction + braid relations to try to reach a sigma-positive word;
completeness via handle reduction. For our witness pair the quotient is simple:
A^-1 B with A=s0^4, B=s0^2 s1^2 s2^2: A^-1B = s0^{-2} s1^2 s2^2. Main generator s0 occurs
only negatively... but word not reduced to sigma-positive form directly; need to check
no equivalent word has main generator only positive. Note B^{-1}A = s2^{-2}s1^{-2}s0^2:
main generator s0 only positive => B^{-1} A is sigma_0-positive => B < A in Dehornoy order,
PROVIDED the word s2^{-2} s1^{-2} s0^2 is already sigma-positive (it is: s0 occurs, only
positively, and no smaller-indexed... s0 IS the smallest (main = smallest index occurring?
Dehornoy: main generator = SMALLEST index? No! Main = LARGEST? Dehornoy order: w is
sigma-positive if the generator with smallest index occurring appears only positively.
Here smallest index in B^{-1}A is 0 (s0), appears only positively. So B^{-1}A is
sigma_0-positive by inspection! Great: B < A rigorously, no reduction needed.
General check below verifies word-problem identity A*(A^-1B)=B via free-group action.
"""
import sys
sys.path.insert(0, 'artifacts')

def free_reduce_word(w):
    st = []
    for g in w:
        if st and st[-1] == -g: st.pop()
        else: st.append(g)
    return st

def artin_action(word, n):
    """Faithful Artin action of B_n on F_n. Represent F words as tuples of ints (1-based gens, neg=inverse), freely reduced.
    sigma_i: x_i -> x_i x_{i+1} x_i^{-1}; x_{i+1} -> x_i; others fixed. (0-based i.)
    Return images of each generator."""
    def apply(img, i, sign):
        # apply sigma_i^{sign} to reduced word img; handle letter signs: f(w^{-1}) = f(w)^{-1}
        def sub_letter(g, sgn):
            a = abs(g) - 1
            neg = (g < 0)
            if sgn > 0:
                if a == i: base = [i+1, i+2, -(i+1)]
                elif a == i+1: base = [i+1]
                else: base = [g]
            else:
                if a == i: base = [i+2]
                elif a == i+1: base = [-(i+2), i+1, i+2]
                else: base = [g]
            if neg and (a == i or a == i+1):
                base = [-x for x in reversed(base)]
            return base
        out = []
        for g in img:
            out += sub_letter(g, sign)
        return free_reduce_word(out)
    imgs = [[k+1] for k in range(n)]
    for g in word:
        i = abs(g) - 1; s = 1 if g > 0 else -1
        imgs = [apply(img, i, s) for img in imgs]
    return [tuple(x) for x in imgs]

def is_identity(word, n):
    return artin_action(word, n) == [tuple([k+1]) for k in range(n)]

def main_index(word):
    """Smallest generator index (0-based) occurring (either sign)."""
    if not word: return None
    return min(abs(g)-1 for g in word)

def is_sigma_positive(word):
    """True if generator with smallest occurring index appears with only one sign and it's positive."""
    if not word: return False
    m = main_index(word)
    signs = {1 if g > 0 else -1 for g in word if abs(g)-1 == m}
    return signs == {1}
