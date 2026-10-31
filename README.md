# Qualitative-behaviour control with uncontrollable linearisation: branching feedback and the geometry of its singularity locus

Alex Shoshitaishvili (also published as A. N. Shoshitaishvili), Independent Researcher

<!-- DOI badge to be added after the first Zenodo release -->

## Abstract

We study feedback synthesis at a working point where the linearisation of the plant is uncontrollable. We recast the qualitative-behaviour control method of the author's papers of 1988-1992 in the language of geometric control. The organising object is the integral manifold M of the plant-reference product system; solvability of the qualitative-behaviour control (QBC) problem, choosing feedback so that the closed loop reproduces the dynamics of a prescribed reference system, is equivalent to M being the graph x = F(z) of a diffeomorphism F, and uncontrollability of the linearisation forces F to be singular whenever the spectrum of the reference does not contain some uncontrollable eigenvalue of the plant. When the inverse of this projection is multivalued, the feedback obtained by inverting it is multivalued, ramifying along the critical value set of that projection. We give the geometry of this set; apply the construction to the nonholonomic (Brockett) integrator, where a weighted blow-up resolves the plant into a family of surfaces on which the synthesis has a half-attraction time that does not depend on the initial point, and where rotating the branch chosen on the axis gives a continuous time-periodic stabiliser of Coron's type; and use the branching feedback to synthesise a periodic motion of prescribed frequency when the critical mode +-i omega_0 is uncontrollable. No smooth feedback can change the frequency omega_0 of this mode; a branching feedback can: for nondegenerate quadratic control terms it produces an attracting cycle with a prescribed frequency from an explicit range, apart from a few resonances with omega_0. A similar branching feedback also makes the working point asymptotically stable for a plant whose linearisation there is uncontrollable and unstable, when its quadratic terms satisfy an explicit sign condition. This is the full version of the short preprint with the same applications.

This is the full version; see also the short preprint *Branching feedback at an uncontrollable linearisation with applications to stabilisation, the Brockett integrator, control of frequency and Hopf bifurcation* (10 pages).

## Files

- `Shoshitaishvili_QualitativeFeedback_Companion.tex` - LaTeX source (amsart; figures are inline TikZ, no external files).
- `Shoshitaishvili_QualitativeFeedback_Companion.pdf` - compiled preprint (pdflatex, 49 pages).

## Building

```
pdflatex Shoshitaishvili_QualitativeFeedback_Companion.tex
pdflatex Shoshitaishvili_QualitativeFeedback_Companion.tex
pdflatex Shoshitaishvili_QualitativeFeedback_Companion.tex
```

## Citing this work

See [`CITATION.cff`](CITATION.cff).

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)

Copyright (c) 2026 Alex Shoshitaishvili
