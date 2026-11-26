# Independent mathematical audit

## correctness

PASS

For two sources, a common received word implies the difference support is contained in the union of the two chosen nonwrapping length-two windows. Conversely, choose the second source's letters on the first window outside the second, the first source's letters on the second outside the first, the common letters off the union, and either on the intersection. The received word need not be proper; this also covers zero or one overwrite change. For 2≤n≤4 the first and last windows cover the word. For n≥5 two sources with the same interior are confusable by those windows, giving the q(q−1)^(n−5) bound. At five the q shifts of (0,1,2,3,4) modulo q are proper even at q=2, and distinct shifts differ at all five coordinates. A fresh output-ball enumeration on the frozen JSON witnesses checked properness and disjoint outputs at lengths 2–7, with full interior coverage at 5–7. The lower bounds therefore match the projected upper bounds, and the first length permitting eight messages is seven. Replay: /workspace/branches/395462f8-1235-4814-8586-fe978cca103c/independent_ball_check.py and independent_ball_check_output.txt in that directory. This is a check of the explicit lower-bound witnesses, not an inference of a general achievability theorem. Uploaded scripts were not executed.

## originality

PASS

The supported distinct claim is the evaluated ternary optimum under the simultaneous proper-source and adjacent-substitution requirements, including the exact length-six and length-seven saturating codebooks and hence the eight-message boundary. The two-window interior bound is a constrained form of the classical burst puncturing argument, and the five-letter shifts alone are routine. The strongest examined catalog comparisons either change the alphabet and source, or change the channel/code property. Primary inspection distinguished relevant constrained-code and structured-error work; the 2012 full text remains an unresolved access risk, not negative evidence or grounds for failure.

## value

PASS

The concrete unknown in this model is whether every proper interior admits a mutually compatible extension at these short lengths. The witnesses permit one-burst protection at the shortest admissible blocklength supporting a three-bit payload, with a rigorous impossibility at every shorter length. This makes the finite cutoff operationally meaningful within the stated mathematical model, rather than crediting the elementary puncturing argument alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
