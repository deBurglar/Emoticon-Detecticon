# Emoticon-Detecticon

A dataset of English Twitter messages with six basic emotions: anger, fear, joy, love, sadness, and surprise. For more detailed information please refer to the paper below.
The authors constructed a set of hashtags to collect a separate dataset of English tweets from the Twitter API belonging to eight basic emotions, including anger, anticipation, disgust, fear, joy, sadness, surprise, and trust. The data has already been preprocessed based on the approach described in their paper.

Homepage: https://github.com/dair-ai/emotion_dataset
Paper: CARER: Contextualized Affect Representations for Emotion Recognition
Point of Contact: ellfae@gmail.com
Size of downloaded dataset files: 3.95 MB
Size of the generated dataset: 4.16 MB
Total amount of disk used: 8.11 MB

An example of 'train' looks as follows.
{
   "label": 0,
   "text": "im feeling quite sad and sorry for myself but ill snap out of it soon"
}


## EVALUAATION METRICS 

| Metric           | Meaning                                                          |
| ---------------- | ---------------------------------------------------------------- |
| **Accuracy**     | Overall correct predictions:                            |
| **Precision**    | How many predicted emotions were correct                         |
| **Recall**       | How well the model finds all relevant cases for each emotion     |
| **F1-score**     | Harmonic mean of precision and recall → balance between them     |
| **Macro avg**    | Simple average across all emotions (treats all emotions equally) |
| **Weighted avg** | Accounts for how frequent each emotion appears                   |



## OBSERVATIONS

-Classes 0 and 1 (likely joy/happy and sadness) are doing very well (F1 > 0.90)

-Classes 2 and 5 have slightly lower recall → model is missing some instances

  Could improve by:

  Trying non-linear kernel (e.g., rbf)

  Hyperparameter tuning (e.g., changing C, gamma)

  Using n-grams in TF-IDF (e.g., ngram_range=(1,2)
