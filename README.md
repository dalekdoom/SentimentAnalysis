# KEN

# NLP

##### Project Guidelines


### ● If you want to work in NLP, the engineering is only

### half the work.

### ● The other half is about:

```
○How tofind andunderstandrelated workonyourproblem
○How todesign effectiveexperimentsandanalyze theirresults
○How tostay outof ethicaltrouble
○How towrite andpublish yourwork (esp. if you are in science)
○How to deploy your system (esp. if you are in business)
```
## Goal


## Pick a topic

- It is highly recommended to not reinvent the wheel from scratch. Therefore, when picking a dataset and
    a topic, it is important to know what existing resources that can be leveraged. Asking the following
    questions to yourself:
       - What is the dataset about? What is the problem? Why this problem interesting and essential?
       - Is there an existing approach? Can you apply this approach to your dataset?
       - How to evaluate your idea/approach? What data can be used for evaluating the proposed approach? Is the data set available?
       - What software packages and resources that you can use for implementing your idea?
       - What is the best and the worse outcomes of the project? (i.e., measure your risk).
       - Who will be your fellow group member? Do they have special expertise? How to split the workload?
- Some possible ways to find a topic are:
    - Take an existing problem we mentioned (or we will mention) in class and come up with some ideas.
    - Take an existing dataset (plenty available) and come up with a task that makes sense to attempt on this dataset.
    - Read a published paper carefully and ask yourself if there is any challenge left from the paper or if you can improve the proposed
       approach.
    - There are many NLP shared tasks atSemeval,CoNLL, and some workshops. A shared task often provides a well-defined problem
       and data set, allowing different teams to fairly compared their approaches. You can use the shared tasks in previous years asa
       testbed of your approaches or participate in a shared task in this year (it is okay if you cannot get the results on the final test
       data set when the semester end. Just evaluate your approach on the development split),


## Project proposal (5%)

- A (maximum) two-page project proposal is due on May 12th (no delays

#### here).

- Pick a title
- State your motivation, your plan, and the expected outcome of your

#### project.

- You can use this chance to draft the introduction and the related work

#### section of your final report.

- You should address the questions in the "Pick a topic" section in your

#### proposal.

- Cite & describe at least 2 pieces of relevant prior work
- Describe the dataset(s) you are going to use
- Outline pre-existing software/tools you are going to use
- Outline preliminary experiments & evaluation methods


## Project report (80%)

- Each team must submit a written project report. You should

### assume the report is structured like a short conference paper.

- If you have a demo system, you can include some screenshots of

### your system.

- It is also recommended to include a discussion of how your research

### work can be further extended.

- It is required to use the provided ACL Latex style files (also

### available in Overleaf) and submit the report in PDF format.

- The report should be no more than 4 pages (plus unlimited pages

### for references).

- A concise and short report is better than a lengthy one.


## Project report (80%)

- Different projects may be graded differently.
    - For example, a project that “reimplements” some proposed approaches and performs

###### comprehensive comparison (e.g. on sentiment analysis on IMDB) might get a high

###### score even if there is no new approach proposed.

- An ambitious idea (e.g. build a chatbot that can replace Jerry) that fails but goes

###### deep into why it failed might also get a high score.

- Here is a general grading rubric:
    - 20% on clarity (Is it clear what was done? Is the report well-written and well-

###### structured? Is the idea well-motivated? Is the literature review comprehensive?)

- 25% on soundness and correctness. (Is the technical approach well-chosen and deep

###### enough? Is the implementation correct?)

- 25% on the meaningful comparison. (Are the experiment settings correct? Are the

###### approaches experimental results correctly interpreted?)

- 10% on novelty and substance. (What are the new things that we can learn from this

###### project?)


## Project pitch + website (15%)

- Each project team is expected to make a ”pitch” (due to time

### shortage) of their project.

- I expect everyone to attend the final project presentation unless

### special circumstances.

- Make a website (github) about your project. Use that to advertise

### your work! Place everything there (your code, your report, your

### figures, etc.)

- The website should highlight your problem, dataset & approach,

### tailored for general audience (include figures, examples, etc.)


### ● For a successful project (in this course and in

### general), you must:

```
○Identifyanopen problem (task or dataset),present a
hypothesisabout it,andsurvey the relevantliterature.
○Design andrun anexperimentto testthat hypothesis.
○Analyzethe resultsto reveal whatyourexperiment tellsus
about yourhypothesis.
```
## Key elements


## The literature review

##### ● Do this early!

```
○ Learnaboutcommonmethods,datasets,andlibraries
thatwill makeyourlifeeasier.
○ Buyyourself moretimetothinkaboutthe questionsthat
have or haven’t beenansweredintheliterature.
```
##### ● How to identify relevant papers

1. Do a keyword search on Google Scholar (or the ACL
    Anthology)
2. Download the papers that seem mostrelevant
3. Skim the abstracts, intros, & previous worksections
4. Identify papers that look relevant, appear often, & have lots
    of citations on Google Scholar
5. Download those papers6.
6. Return to step 3


## Anatomy of an NLP paper

● You get to deliver four pages because you are doing less work!


## Writing a paper is like

## composing a piece of art

- Write clearly. A good paper is direct, unambiguous and describes all stages of

##### the work in complete—but not superfluous—detail. Quality of writing will

##### affect your grade.

- All plots, figures, and tables must have a title, labeled axes and a caption.

##### There should be no confusion about what you’re trying to express, or why

##### the plot was included.

- Do not include multiple figures that all convey the same information. Be

##### succinct.

- Avoid redundancy. Do not describe the same component of your work twice.
- Do not include much code in your report. If your approach contains a new

##### algorithm you developed, it may be appropriate for you to include its

##### pseudocode, but do not copy and paste code from your editor. Do not

##### include well-known algorithms. Cite when appropriate.


## The literature review

```
● Where to find the most trustworthy papers:
○ NLP and Computational Linguistics: Proceedings of ACL conferences
(ACL,NAACL,EACL,EMNLP,CoNLL),TACL, Computational
Linguistics ,arXiv*
○ MachineLearning/AI:ProceedingsofNIPS,ICML,ICLR,AAAI, IJCAI,
andarXiv*
● You’ll have to use your judgment in deciding which papers to
read, and which papers to trust.
○ Paperscandisagreewithoneanother.
○ Youmightjustfindtoomanypapers.
```
```
* Official (reasonable) ACL policy: arXiv papers are prior work and should be in literature
reviews and comparison tables, but you can still treat claims from those papers moreskeptically.
```

## The literature review

```
● Which papers will be most useful?
○ Newerones,especiallyiftheycitetheolderpapersthatyou’re interestedin.
■ Thenewerpapermightcontainagoodsummaryoftheolder one!
○ Paperspublishedintopconferencesandjournals,ratherthanarXiv papersor
paperspublishedelsewhere.
■ Reviewershavecarefullylookedatthesepapersformistakes or
inconsistencies.
○ Published papers with negative results (method X doesn’t work, methodX
doesn’t dowhatyouthinkitdoes,...),ratherthanpapers with positiveresults.
■ Negativeresultsareusuallyheldtoahigherstandardinfor publishing.
```

## The Hypothesis

```
○ Bad/unfalsifiable:
■ Neuralnetworksaremoreelegantandprincipled thanfeature-
based systems forsentiment analysis.
○ Falsifiable butuninformative:
■ My convolutional neural network (CNN) model outperforms the Socher
etal.(2015)baselineontheStanfordSentimentTreebank data.
○ Typical goodpaper:
■ CNNmodelsoutperformfeature-basedsystemsonsentiment analysis
forreviews.
○ Ambitiouspaper:
■ Non-professionalwebuserstendto expresssentimentusing aset of
common fixed phrases when they discuss products. These phrases vary
enoughthatsimplesymbolicfeaturesdon’tcapture themwell,but
they’restructuredenoughthatfilter-basedneural networkslikeCNNs
cancapturethemveryefficiently.
```

## Controlled experiments

- Your experiment needs to test your hypothesis.

### Everything that you’ve learned about controlled

### experimentation applies in NLP.

- Example results on a classification problem:

### ● Paper A: BOW-NB gets 77.6%

### ● Paper B: Word2Vec-LSTM gets 77. 9 %

- What can you conclude?


## Baselines

### ● Baseline can mean any of three things, and

### you usually want all three:

```
○ Anyone’sperformance numbersfor simplestreasonable
approach to yourproblem (CBOW,logisticregression, plan
seq2seq).
○ Your numbers for a reasonably competitive system based on
existingideas. Thiscanbe based onapublishedsystemor your
own work,butyou should makeaprecise,controlled
comparisonwith it.
○ The best publishednumber foryourproblem. It’scommon to
notbeat this,butyou should compare withit.Thisis what
couldgiveyou the rightto claimthe ‘stateoftheart’.
```

## Upper bounds

### ● Less necessary, but often helpful: Measure (or

### find out) the accuracy of a human annotator!

```
○Youcan’t usethe sameannotations that youused to create
the data.
○It’sbetterif youdon’teven use the samepeople.(Why?)
```
### ● 77% accuracy doesn’t look so bad if a human

### only gets 81%!


## Datasets

```
● You’ll want real natural language data for any NLP project.
(for a publication, you’ll usually want multiple datasets)
● You’ll almost always want to use at least one dataset that
appeared in related prior work, even if you’re the first one to
solve a specific problem.
○ WorkingonsentimentanalysisinPortuguese?
■ ShowthatyourmethodiscompetitiveonEnglishdatasetslike SST or
IMDB.
■ CollectorcreateadatasetforPortuguese.
■ Showresultsonthenewdatawithyourmethodandseveral existing
baselines.
```

## Getting datasets

```
● Find them!
○ TheACLanthology!
○ Kaggle
○ ...
● Buildthem!
○ Write very detailed notes on what you do and why: Readers and reviewerswill
assumethatallof yourdecisionsarebiasedtothat unfairlyfavorsthesystemsyou’re
interestedin.Toconvincethem that you didn’t, you’ll need to show that you made
fair and reasonabledecisions.
● Scrape them?
○ It’seasytobreakthelawthisway.Orgettemporarilybanned from
Twitter/eBay/Reddit/Tinder/etc.
○ Forsomeslightlydateddiscussionofscraping,see:
http://nlp.stanford.edu/IR-book/
```

## Getting datasets

```
● Have someone else build them!
○ Write simple annotationguidelinesthatnon-NLPerscanfollow.
■ Youstillneedtoconvinceyourreviewerstheseguidelines aren’t
unfairlyadvantagingyourmethod.
○ PaysomefriendsorMechanicalTurk(MTurk)workerstofollow your
guidelines.
○ Thisisoftenquickandcheapinpractice.Ballparkcosts(at
$10–20/hr):
■ Writing:~$0.05–$0.25persentencewritten
■ Labeling:~$0.02–$0.15persentenceread
○ Someadvice:
■ Tryyourannotationtaskyourselfforhalfanhour.
■ Communicate with your annotators! Even on MTurk, they’ll oftenbe
tryinghardtounderstandyourtask,andyouwantto beavailableifthey
havequestionsoriftheyseeissues.
```

## Getting datasets

```
● Have someone else build them!
○ Someadvice:
■ Tryyourannotationtaskyourselfforhalfanhour.Ifthere’s anythingthat
youfindconfusingorfrustrating,fixit!
■ Communicate with your annotators! Even on MTurk, they’ll oftenbe
tryinghardtounderstandyourtask,andyouwantto beavailableifthey
havequestionsoriftheyseeissues.
○ For thisclass:
■ You’rewelcometouseMTurk if youhaveaccesstoit and you can cover it
(DO NOT SPEND MONEY ON THIS, GET DRINKS INSTEAD).
■ Otherwise, consider trading data with another team, and havingthe
membersoftheotherteamannotateyourdata.
■ Don’ttellthemtoomuchaboutyourproject—justsharethe annotation
guidelines.
```

## Quantitative evaluation

```
● This is a huge topic, but in short:
○ Followpriorwork precisely inhowyouchooseandimplementyour
main evaluationmetric.
○ Do showmetricsasmanyvariantsofyourmodelasyoucan
(ablationanalysis).
■ Example:
● BOW-NB classifier with no pre-processing
● BOW-NB classifier with pre-processing
● BOW-LR classifier with no pre-processing
● BOW-LR classifier with pre-processing
■ Shouldyouusethedevsetorthetestset?
○ Do usecarefully-designedhumanevaluationsfortaskswherethisis
standard(e.g. summarization).
```

## Quantitative evaluation

```
● This is a huge topic, but in short:
○ Do inventnewanalysismetricsiftheyhelpyoumakeyourpoint.
■ Ifyoursystemgoodatclassifyinglongsentences,alsoreport
accuracyonthesubsetofsentencesoflength>20.
■ If your baseline for a text generation task only uses very
common words, and your system fixes that, measure the
averagefrequency ofthewordsthateachsystemgenerates.
■ Don’t talkaboutthe ‘stateoftheart’forthingsthatnobody
elsemeasures.
○ Do performextrinsicevaluationsondownstreamtasksifyouexpect
the output of your system to be used as the input to any other
system.
```

## Quantitative evaluation

```
● This is a huge topic, but in short:
○ Do explicitlytestforstatisticalsignificance,especiallywhenyour
hypothesis depends on a small difference or when model
performance is highly variable. (See Resnik and Lin reading or Berg-
Kirkpatricketal.‘12)
■ Methods here vary widely within NLP, but don’t expect people
(or me J)totakeyouseriouslyifthemainclaimofyourpaperis
that you get an 0.2% accuracy improvement on the state of the
art.
■ Remember what we discussed about evaluation metrics &
cross-validation
```

## Quantitative Evaluation

```
● If your system doesn’t beat your baselines, or if the differences between your
results aren’t significant: Say so! And explain what you found!
○ Well-presentednegativeresultsdomovethefieldforward,andareincommoninprojectslike classpapers
thathavetohappeninashorttime.
```

## Qualitative evaluation

## and error analysis

```
● NLP papers generally have an analysis section.
○ Thismaybecalledsomethingelse!
● Your goal here: Convince the reader of your hypothesis.
● If your hypothesis is interesting, it’ll be hard toevaluate
with standard/intuitive quantitative metrics.
○ Non-professional web users tend to express sentiment using a set of common fixedphrases
whentheydiscussproducts.Thesephrasesvary enough that simple symbolic features don’t
capture them well, but they’re structured enough that filter-based neural networks like
CNNs cancapturethemveryefficiently.
```

## Qualitative evaluation

## and error analysis

```
● So, give the reader qualitative evidence, too!
● Places to start:
○ Looktopriorwork,anddowhattheydo.
○ Showexamplesofsystemoutput.
○ Comeupwith categories todescribesystemerrorsandcount
them.
○ VisualizeyourhiddenstateswithtoolslikeLSTMVis.
○ Plothowyourmodelperformancevarieswithamountof
data.
○ Build a demo!
```

## Formative vs. summative

## evaluation

```
When the cook tastes the soup, that’s formative; when the customer
tastes the soup, that’s summative.
```
```
● Formative evaluation: guiding further investigations
○ Typically:lightweight,automatic,intrinsic
○ ComparedesignoptionAtooptionB
○ Tunehyperparameters:smoothing,weighting,learningrate
● Summative evaluation: reporting results
○ Compareyourapproachtopreviousapproaches
○ Comparedifferent major variantsofyourapproach
○ Onlyusethetestsethere
○ Generallyonlybotherwithhumanorextrinsicevaluationshere
● Potential serious mistake: Don’t save all your qualitative evaluation
for the summative evaluation!
```
Resnik and Lin on evaluation


## Typesetting

## and LaTeX

● You’ll need to use the _LaTeX_ typesetting tool to write your paper.

● For the basics of LaTeX, there are good tutorials online.

● Another good source of handy tricks:


