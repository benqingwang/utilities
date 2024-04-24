true_labels = [0, 1, 0, 1, 0, 1]
predicted_labels = [0, 1, 0, 0, 0, 1]


from sklearn.metrics import confusion_matrix

# Compute the confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels)
print("Confusion Matrix:\n", conf_matrix)

"""
[[TN, FP],
 [FN, TP]]
 """

from sklearn.metrics import f1_score

# Compute the F1 score
f1 = f1_score(true_labels, predicted_labels)
print("F1 Score:", f1)


from sklearn.metrics import classification_report

# Generate a classification report
report = classification_report(true_labels, predicted_labels)
print("Classification Report:\n", report)
