import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score

plt.rc("axes.spines", top=False, right=False)
plt.rc("font", size=13)
plt.rc("figure", figsize=(12, 8.5))
plt.rc("axes", grid=True)
plt.rc("grid", lw=0.8, color="grey", ls=":", alpha=0.7)


def evaluate_threshold(t, y, probs):
    '''
    Returns dictionary of model evaluation scores
    '''
    yhat = (probs > t).astype(int)
    return {
        "threshold": t,
        "precision": precision_score(y, yhat),
        "recall": recall_score(y, yhat),
        "accuracy": accuracy_score(y, yhat),
    }


def evaluate_thresholds(y, probs):
    '''
    Returns dataframe of model evaluation scores over range of 0 to 1 by .01
    '''
    return pd.DataFrame(
        [evaluate_threshold(t, y, probs) for t in np.arange(0, 1.01, 0.01)]
    )


def plot_metrics_by_thresholds(y, probs, subplots=False):
    '''
    Returns plot of model evaluation scores
    '''
    evaluation = evaluate_thresholds(y, probs)
    axs = (
        evaluation.query("precision > 0")
        .set_index("threshold")
        .plot(subplots=subplots, sharex=True, sharey=True, figsize=(12, 8.5))
    )
    (axs[-1] if subplots else axs).set_xticks(np.arange(0, 1.05, 0.05))
    plt.tight_layout()
