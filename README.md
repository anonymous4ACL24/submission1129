# submission1129

The source code of VulLibGen is included in `VulLibGen-code` (details in  `VulLibGen-code/ReadMe.md`).
The dataset of VulLibGen is included in `VulLibGen-dataset` (details in  `VulLibGen-dataset/ReadMe.md`).

The comparison results between VulLibGen and our baselines on Precision, Recall, F1 is included in `prec-rec-f1.csv`.

The status of our submitted <vulnerability, package> pairs is included in `submit-packages-appendix.csv`, and as of today, 38 of them are merged.


### Revision Details

We have greatly benefited from all the comments and suggestions. In revising this paper, we have conducted additional experiments and made major changes to address the comments and suggestions raised by each reviewer. The revised paper is available in our anonymous link: https://github.com/anonymous4ACL24/submission1129/blob/main/VulLibGen-acl24.pdf Here is a summary of the major changes:

1. **Adding more clear details regarding importance/novelty** (Reviewer MzNm and sXy1) 

   This is the main concern of Reviewer MzNm and sXy1. In this revision, we refine our abstract and introduction to clarify the importance and novelty of our work (Lines 1-131).

2. **Evaluating all programming languages for the real world evaluation** (Reviewer MzNm)

   We further submit 32 pairs of <vulnerability, affected package> on the rest three programming languages, JavaScript, Python, and Go (details in our anonymous link: https://github.com/anonymous4ACL24/submission1129/blob/main/submit-packages-appendix.csv). Therefore, we have submitted 60 <vulnerability, affected package> pairs (including all programming languages considered in this paper).

3. **Adding Tables of Recall@1, F1@1 for apples to apples comparison to Chen 2023** (Reviewer BzLa)

   We add the evaluation results of VulLibGen and baselines Precision@1, Recall@1, and F1@1 to keep the same setting as Chen 2023 in Section 10.2 (Tables 7 and Table 8).

4. **Clarifying the rationale of dataset choice** (Reviewer sXy1)

   We clarify our dataset selection and construction: our dataset extends the existing dataset VulLib from Java to all four programming languages. We also explain why we do not use another dataset VeraCode (Lines 329-344 and FootNote 7). 

5. **Adding significance tests for local search and RAG** (Reviewer MzNm)

   We conduct statistical tests on the effectiveness of our RAG and local search algorithm in Section 10.3 (Table 11 and Table 12) to illustrate the significance of the improvement of VulLibGen's each component. We further analyze why local search's improvement is less significant for JS and Python (Line 505-517). 

6. **Adding limitation discussions regarding Token length and number of unique packages** (Reviewer BzLa)

   We explain the limitation of VulLibGen in generating long and complex package names (Lines 629-647 and Table 6).

