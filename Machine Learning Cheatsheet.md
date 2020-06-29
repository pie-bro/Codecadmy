Beautiful Soup Object and Methods
BeautifulSoup uses a parser to take in the content of a webpage. It provides tree traversal and advanced searching methods. It creates an object from the website contents.

# This line of code creates a BeautifulSoup object from a webpage:

soup = BeautifulSoup(webpage.content, "html.parser")

# Within the `soup` object, tags can be called by name:

first_div = soup.div

# or by CSS selector:

all_elements_of_header_class = soup.select(".header")

# or by a call to `.find_all`:

all_p_elements = soup.find_all("p")


Beautiful Soup Traversal
BeautifulSoup is a Python library used to parse and traverse an HTML page. Beautiful Soup can scrape webpage data and collect it in a form suitable for data analytics.


Linear Regression
Gradient descent step
The size of the step that gradient descent takes is called the learning rate. Finding an adequate value for the learning rate is key to achieve convergence. If this value is too large the algorithm will never reach the optimus, but if is too small it will take too much time to achieve the desired value.

Gradient Descent in Regression
Gradient Descent is an iterative algorithm used to tune the parameters in regression models for minimum loss.


Classification: K-Nearest Neighbors

K-Nearest Neighbors Underfitting and Overfitting
The value of k in the KNN algorithm is related to the error rate of the model. A small value of k could lead to overfitting as well as a big value of k can lead to underfitting. Overfitting imply that the model is well on the training data but has poor performance when new data is coming. Underfitting refers to a model that is not good on the training data and also cannot be generalized to predict new data.

KNN Classification Algorithm in Scikit Learn
Scikit-learn is a very popular Machine Learning library in Python which provides a KNeighborsClassifier object which performs the KNN classification. The n_neighbors parameter passed to the KNeighborsClassifier object sets the desired k value that checks the k closest neighbors for each unclassified point.

The object provides a .fit() method which takes in training data and a .predict() method which returns the classification of a set of data points.

from sklearn.neighbors import KNeighborsClassifier

KNNClassifier = KNeighborsClassifier(n_neighbors=5)
KNNClassifier.fit(X_train, y_train)
KNNClassifier.predict(X_test)

Euclidean Distance
The Euclidean Distance between two points can be computed, knowing the coordinates of those points.

On a 2-D plane, the distance between two points p and q is the square-root of the sum of the squares of the difference between their x and y components. Remember the Pythagorean Theorem: a^2 + b^2 = c^2 ?

We can write a function to compute this distance. Let’s assume that points are represented by tuples of the form (x_coord, y_coord). Also remember that computing the square-root of some value n can be done in a couple of ways: math.sqrt(n), using the math library, or n ** 0.5 (n raised to the power of 1/2).

def distance(p1, p2):
  x_diff_squared = (p1[0] - p2[0]) ** 2
  y_diff_squared = (p1[1] - p2[1]) ** 2
  return (x_diff_squared + y_diff_squared) ** 0.5

distance( (0, 0), (3, 4) )      # => 5.0
Euclidean Distance between two points p and q.
Elbow Curve Validation Technique in K-Nearest Neighbor Algorithm
Choosing an optimal k value in KNN determines the number of neighbors we look at when we assign a value to any new observation.

For a very low value of k (suppose k=1), the model overfits on the training data, which leads to a high error rate on the validation set. On the other hand, for a high value of k, the model performs poorly on both train and validation set. When k increases, validation error decreases and then starts increasing in a “U” shape. An optimal value of k can be determined from the elbow curve of the validation error.

K-Nearest Neighbors
The K-Nearest Neighbors algorithm is a supervised machine learning algorithm for labeling an unknown data point given existing labeled data.

The nearness of points is typically determined by using distance algorithms such as the Euclidean distance formula based on parameters of the data. The algorithm will classify a point based on the labels of the K nearest neighbor points, where the value of K can be specified.

KNN of Unknown Data Point
To classify the unknown data point using the KNN (K-Nearest Neighbor) algorithm:

Normalize the numeric data
Find the distance between the unknown data point and all training data points
Sort the distance and find the nearest k data points
Classify the unknown data point based on the most instances of nearest k points
Normalizing Data
Normalization is a process of converting the numeric columns in the dataset to a common scale while retaining the underlying differences in the range of values.

For example, Min-max normalization converts each value of the numeric column to a value between 0 and 1 using the formula Normalized value = (NumericValue - MinValue) / (MaxValue - MinValue). A downside of Min-max Normalization is that it does not handle outliers very well.


K Nearest Neighbor Regression

Regression in KNN Algorithm
K-Nearest Neighbor algorithm uses ‘feature similarity’ to predict values of any new data points. This means that the new point is assigned a value based on how closely it resembles the points in the training set. During regression implementation, the average of the values is taken to be the final prediction, whereas during the classification implementation mode of the values is taken to be the final prediction.


Logistic Regression


Scikit-Learn Logistic Regression Implementation
Scikit-Learn has a Logistic Regression implementation that fits a model to a set of training data and can classify new or test data points into their respective classes. All important parameters can be specified, as the norm used in penalizations and the solver used in optimization.

Logistic Regression sigmoid function
Logistic Regression models use the sigmoid function to link the log-odds of a data point to the range [0,1], providing a probability for the classification decision. The sigmoid function is widely used in machine learning classification problems because its output can be interpreted as a probability and its derivative is easy to calculate.

Classification Threshold definition
A Classification Threshold determines the cutoff where the probabilistic output of a machine learning algorithm classifies data samples as belonging to the positive or negative class. A Classification Threshold of 0.5 is well suited to most problems, but particular classification problem could need a fine-tuned threshold in order to improve overall accuracy.

Logistic Regression interpretability
Logistic Regression models have high interpretability compared to most classification algorithms due to optimized feature coefficients. Feature coefficients can be thought as a measure of sensitivity in feature values.

Log-Odds calculation
The product of the feature coefficients and feature values in a Logistic Regression model is the Log-Odds of a data sample belonging to the positive class. Log odds can take any real value and it’s an indirect way to express probabilities.

Logistic Regression Classifier
Logistic Regression is supervised binary classification algorithm used to predict binary response variables that may indicate the presence or absence of some state. It is possible to extend Logistic Regression to multi-class classification problems by creating several one-vs-all binary classifiers. In a one-vs-all scheme, n - 1 classes are grouped as one and a classifier learns to discriminate the remaining class from the ensembled group.

Logistic Regression prediction
Logistic Regression models predict the probability of an n-dimensional data point belonging to a specific class by constructing a linear decision boundary. This decision boundary splits the n-dimensional plane in two. In a prediction stage, the point is classified according to which semiplane has the highest probability.

Logistic Regression cost function
The cost function measuring the inaccuracy of a Logistic Regression model across all samples is Log Loss. The lower this value, the greater the overall classification accuracy. Log Loss is also known as Cross Entropy loss.


Decision Trees

Information Gain at decision trees
When making decision trees, two different methods are used to find the best feature to split a dataset on: Gini impurity and Information Gain. An intuitive interpretation of Information Gain is that it is a measure of how much information the individual features provide us about the different classes.

Gini impurity
When making decision trees, calculating the Gini impurity of a set of data helps determine which feature best splits the data. If a set of data has all of the same labels, the Gini impurity of that set is 0. The set is considered pure. Gini impurity is a statistical measure - the idea behind its definition is to calculate how accurate it would be to assign labels at random, considering the distribution of actual labels in that subset.

Decision trees leaf creation
When making a decision tree, a leaf node is created when no features result in any information gain. Scikit-Learn implementation of decision trees allows us to modify the minimum information gain required to split a node. If this threshold is not reached, the node becomes a leaf.

Optimal decision trees
Creating an optimal decision tree is a difficult task. For example, the greedy approach of splitting a tree based on the feature that results in the best current information gain doesn’t guarantee an optimal tree. There are numerous heuristics to create optimal decision trees, and each of these methods proposes a unique way to build the tree.

Decision Tree Representation
In a decision tree, leaves represent class labels, internal nodes represent a single feature, and the edges of the tree represent possible values of those features.

Unlike other classifiers, this visual structure gives us great insight about the algorithm performance.

Decision trees pruning
Decision trees can be overly complex which can result in overfitting. A technique called pruning can be used to decrease the size of the tree to generalize it to increase accuracy on a test set. Pruning is not an exact method, as it is not clear which should be the ideal size of the tree. This technique can be made bottom-up (starting at the leaves) or up-bottom (starting at the root).

Decision Trees Construction
Decision Trees are usually constructed from top to bottom. At each level of the tree, the feature that best splits the training set labels is selected as the “question” of that level. Two different criteria are available to split a node, Gini Index and Information Gain. The convenience of one or the other depends on the problem.

Random Forest definition
A Random Forest Classifier is an ensemble machine learning model that uses multiple unique decision trees to classify unlabeled data. If compared to an individual decision tree, Random Forest is a more robust classifier but its interpretability is reduced.

Random Forest overfitting
Random Forests are used to avoid overfitting. By aggregating the classification of multiple trees, having overfitted trees in the random forest is less impactful. Reduced overfitting translates to greater generalization capacity, which increases classification accuracy on new unseen data.

Random Forest feature consideration
When creating a decision tree in a random forest, a random subset of features are considered as the best feature to split the data on. By splitting the data in a random subset of features, all estimators are trained considering different aspects of the data, which reduces the probability of overfitting.

Random Forest aggregative performance
A random forest classifier makes its classification by taking an aggregate of the classifications from all the trees in the random forest. For classification, this aggregate is a majority vote. For regression, this could be the average of the trees in the random forest. This aggregation allows the classifier to capture complex non-linear relations from the data. The model performance is far superior than a linear model.

Bagging at Random Forest
Trees in a random forest classifier are created by using a random subset of the original dataset with replacement. This process is known as bagging. Bagging prevents overfitting, given that each individual tree is trained on a subset of original data.


Classification: Naive Bayes

Statistical Dependence
In statistics, two events are dependent if the occurrence of one of the events causes the probability of the other event occurring to change in a predictable way.

Bayes Theorem
Bayes Theorem calculates the probability of A given B as the probability of B given A multiplied by the probability of A divided by the probability of B:

P(A|B)= {P(B|A)*P(A)​}/{P(B)}
This theory describes the probability of an event (A), based on prior knowledge of conditions (P(B|A)) that might be related to the event.

Statistical Independence
In statistics, two events are independent if the probability of one event occurring does not affect the probability of the second event occurring.


Artificial Intelligence Decision Making: Minimax

Minimax algorithm state value
When writing the minimax algorithm, each game involves two players and game states can be evaluated as a value. One of the players is called the maximizer, because he or she wants to maximize the value of the game and the remaining player is called the minimizer.

Minimax algorithm problem specification
Given a game state, the minimax algorithm finds the decision that maximizes the minimum gain. In other words, if you assume your opponent will make decisions that minimize your gain, the algorithm finds the move that will maximize it based on the options your opponent gives you. It is assumed that the game is being played by turns and that the opponent is playing optimally, this is: at each turn a player must make a move, and this move is the best the player can make in that situation.

Minimax algorithm assumption
When running the minimax algorithm, it is assumed that your opponent is playing optimally. This assumption is a worst case scenario, given that if your opponent is not playing optimally the problem is reduced to a simpler one.

Minimax algorithm game representation
When writing the minimax algorithm, a game is modeled as a tree. Different elements of the game (as the current state and all possible moves) are represented as different parts of the tree. This visual representation of the game is a great aid in order to implement the minimax algorithm.

Minimax algorithm state evaluation
When running the minimax algorithm, a game state can be evaluated even if it is not a leaf. This game state evaluation is particularly important in some games such as chess, where we have a long sequence of states before reaching a leaf.

Minimax algorithm size restriction
The size of the game tree is a very important restriction in a minimax algorithm, given that it is not possible to visit all states in a reasonable time. If the maximum depth you can consider is reduced, the optimality of your solution is affected. When the size of the game tree is very large, several heuristics can be applied to find a good solution of the minimax algorithm.

Minimax algorithm with alpha-beta pruning
When implementing alpha-beta pruning in the minimax algorithm, its execution time is drastically decreased. For a given unit of time, a minimax algorithm with alpha-beta pruning can go down twice as far as a minimax algorithm without this pruning technique.

Alpha-beta pruning variables
When using alpha-beta pruning in a minimax algorithm, it is needed to track the value of two different variables (alpha and beta) in order to decide when to prune a part of the tree. At the beginning of the game, alpha is equal to negative infinity and beta is equal to positive infinity. These values are updated as the game progresses.


Clustering: K-Means

K-Means: Inertia
Inertia measures how well a dataset was clustered by K-Means. It is calculated by measuring the distance between each data point and its centroid, squaring this distance, and summing these squares across one cluster.

A good model is one with low inertia AND a low number of clusters (K). However, this is a tradeoff because as K increases, inertia decreases.

To find the optimal K for a dataset, use the Elbow method; find the point where the decrease in inertia begins to slow. K=3 is the “elbow” of this graph.


Unsupervised Learning Basics
Patterns and structure can be found in unlabeled data using unsupervised learning, an important branch of machine learning. Clustering is the most popular unsupervised learning algorithm; it groups data points into clusters based on their similarity. Because most datasets in the world are unlabeled, unsupervised learning algorithms are very applicable.

Possible applications of clustering include:

Search engines: grouping news topics and search results
Market segmentation: grouping customers based on geography, demographics, and behaviors
K-Means Algorithm: Intro
K-Means is the most popular clustering algorithm. It uses an iterative technique to group unlabeled data into K clusters based on cluster centers (centroids). The data in each cluster are chosen such that their average distance to their respective centroid is minimized.

Randomly place K centroids for the initial clusters.
Assign each data point to their nearest centroid.
Update centroid locations based on the locations of the data points.
Repeat Steps 2 and 3 until points don’t move between clusters and centroids stabilize.


K-Means Algorithm: 2nd Step
After randomly choosing centroid locations for K-Means, each data sample is allocated to its closest centroid to start creating more precise clusters.

The distance between each data sample and every centroid is calculated, the minimum distance is selected, and each data sample is assigned a label that indicates its closest cluster.

The distance formula is implemented as .distance()and used for each data point.

np.argmin() is used to find the minimum distance and find the cluster at that distance.

# distance formula
def distance(a, b):
  one = (a[0] - b[0]) **2
  two = (a[1] - b[1]) **2
  distance = (one+two) ** 0.5
  return distance
Scikit-Learn Datasets
The scikit-learn library contains built-in datasets in its datasets module that are often used in machine learning problems like classification or regression.

Examples:

Iris dataset (classification)
Boston house-prices dataset (regression)
The format of these datasets are important to their use with algorithms. For example, each piece of data in the Iris dataset is a sample (flower type), and each element within a sample is a feature (i.e. petal width).


K-Means Using Scikit-Learn
Scikit-Learn, or sklearn, is a machine learning library for Python that has a K-Means algorithm implementation that can be used instead of creating one from scratch.

To use it:

Import the KMeans() method from the sklearn.cluster library to build a model with n_clusters

Fit the model to the data samples using .fit()

Predict the cluster that each data sample belongs to using .predict() and store these as labels

from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)

model.fit(data_samples)

labels = model.predict(data_samples)
Cross Tabulation Overview
Cross-tabulations involve grouping pieces of data together in order to examine their relationship in a different way. Sometimes correlations within data can be seen better when not just looking at total responses.

This technique is often performed in Python after running K-Means; the Pandas method .crosstab() allows for comparison between resulting cluster labels and user-defined labels for each data sample. In order to validate the results of a K-Means model with this technique, there must be user-defined labels for all data samples.

import pandas as pd

cross_tab = pd.crosstab(df['pred_labels'], df['user_labels'])
K-Means: Reaching Convergence
In K-Means, after placing K random centroids, the data samples are repeatedly assigned to the nearest centroid and then centroid locations are updated. This continues until each of the centroids’ coordinates converge, or stop changing.

This sequence of events can be implemented in Python using a while loop. The loop continues until the difference between each element of the updated centroids and each element of the past centroids_old is 0. This will mean the centroids have converged and the clusters are complete!


K-Means Algorithm: 3rd Step
The third step of K-Means updates centroid locations. After the data are assigned to their respectively closest centroid in step 2, each cluster center location is adjusted to be the average of its assigned data points.

The NumPy .mean() function is used to find the average x and y-coordinates of all data points for each cluster and store these as the new centroid locations.


K-Means Algorithm: 1st Step
The first step of the K-Means clustering algorithm requires placing K random centroids which will become the centers of the K initial clusters. This step can be implemented in Python using the Numpy random.uniform() function; the x and y-coordinates are randomly chosen within the x and y ranges of the data points.


Perceptrons

Perceptron Bias Term
The bias term is an adjustable, numerical term added to a perceptron’s weighted sum of inputs and weights that can increase classification model accuracy.

The addition of the bias term is helpful because it serves as another model parameter (in addition to weights) that can be tuned to make the model’s performance on training data as good as possible.

The default input value for the bias weight is 1 and the weight value is adjustable.

weighted_sum = x1*w1 + x2*w2 + x3*w3 + 1*wbias


Perceptrons as Linear Classifiers
At the end of successful training, a perceptron is able to create a linear classifier between data samples (also called features). It finds this decision boundary by using the linear combination (or weighted sum) of all of the features. The perceptron separates the training data set into two distinct sets of features, bounded by the linear classifier.


Adjusting Perceptron Weights
The main goal of a perceptron is to make accurate classifications. To train a model to do this, perceptron weights must be optimizing for any specific classification task at hand.

The best weight values can be chosen by training a perceptron on labeled training data that assigns an appropriate label to each data sample (feature). This data is compared to the outputs of the perceptron and weight adjustments are made. Once this is done, a better classification model is created!

training_set = {(18, 49): -1, (2, 17): 1, (24, 35): -1, (14, 26): 1, (17, 34): -1}


Perceptron Weighted Sum
The first step in the perceptron classification process is calculating the weighted sum of the perceptron’s inputs and weights.

To do this, multiply each input value by its respective weight and then add all of these products together. This sum gives an appropriate representation of the inputs based on their importance.

inputs = [x1,x2,x3]
weights = [w1,w2,w3]
weighted_sum = x1*w1 + x2*w2 + x3*w3


Optimizing Perceptron Weights
To increase the accuracy of a perceptron’s classifications, its weights need to be slightly adjusted in the direction of a decreasing training error. This will eventually lead to minimized training error and therefore optimized weight values.

Each weight is appropriately updated with this formula:

weight = weight + (error * input)weight=weight+(error∗input)

Introduction to Perceptrons
Perceptrons are the building blocks of neural networks. They are artificial models of biological neurons that simulate the task of decision-making. Perceptrons aim to solve binary classification problems given their input.

The basis of the idea of the perceptron is rooted in the words perception (the ability to sense something) and neurons (nerve cells in the human brain that turn sensory input into meaningful information).


Perceptron Activation Functions
The second step of the perceptron classification process involves an activation function. One of these special functions is applied to the weighted sum of inputs and weights to constrain perceptron output to a value in a certain range, depending on the problem.

Some example ranges are [0,1], [-1,1], [0,100].

The sign activation function is a common activation function that contains the perceptron output to be either 1 or -1:

If weighted sum > 0, return 1.
If weighted sum < 0, return -1.

Perceptron Training Error
Training error is the measure of how accurate a perceptron’s classification is for a specific training data sample. It essentially measures “how bad” the perceptron is performing and helps determine what adjustments need to be made to the weights of that sample to increase classification accuracy.

training_error = actual_label - predicted_labeltraining 
e
​	 rror=actual 
l
​	 abel−predicted 
l
​	 abel
The goal of a perceptron is to have a training error of 0; this indicates that a perceptron is performing well on a data sample.

Actual Label	Predicted Label	Training Error
+1	+1	0
+1	-1	2
-1	-1	0
-1	+1	-2
Perceptron Main Components
Perceptrons use three main components for classification:

Input: Numerical input values correspond to features. i.e. [22, 130] could represent a person’s age & weight features.

Weights: Each feature has a weight assigned; this determines the feature’s importance. i.e. In a class, homework might be weighted 30%, but a final exam 50%. Therefore the final is more important to the overall grade (output).

Output: This is computed using inputs and weights. Output is either binary (1,0) or a value in a continuous range (70-90).


Natural Language Processing

Natural Language Processing
Natural language processing (NLP) is concerned with enabling computers to interpret, analyze, and approximate the generation of human speech. Typically, this would refer to tasks such as generating responses to questions, translating languages, identifying languages, summarizing documents, understanding the sentiment of text, spell checking, speech recognition, and many other tasks. The field is at the intersection of linguistics, AI, and computer science.

Language Models
Language models are probabilistic machine models of language used for NLP comprehension tasks. They learn a probability of word occurrence over a sequence of words and use it to estimate the relative likelihood of different phrases. This is useful in many applications, such as speech recognition, optical character recognition, handwriting recognition, machine translation, spelling correction, and many other applications.

Common language models include:

Statistical models
Bag of words (unigram model)
applications include term frequency, topic modeling, and word clouds
n-gram models
Neural Language Modeling (NLM).
Natural Language Toolkit
Natural Language Toolkit (NLTK) is a Python library used for building Python programs that work with human language data for applying in statistical natural language processing (NLP).

NLTK contains text processing libraries for tokenization, parsing, classification, stemming, tagging and semantic reasoning. It also includes graphical demonstrations and sample data sets for NLP.

Text Similarity in NLP
Text similarity is a facet of NLP concerned with the similarity between texts. Two popular text similarity metrics are Levenshtein distance and cosine similarity.

Levenshtein distance, also called edit distance, is defined as the minimum number of edit operations (deletions, insertions, or substitutions) required to transform a text into another.

Cosine similarity measures the cosine of the angle between two vectors. To determine cosine similarity, text documents need to be converted into vectors.

Language Prediction in NLP
Language prediction is an application of NLP concerned with predicting language given preceding language.

Auto-suggest and suggested replies are common forms of language prediction. Common approaches inlcude:

n-grams using Markov chains,
Long Short Term Memory (LSTM) using a neural network.


Bag-of-Words Language Model

Bag-of-words
Bag-of-words(BoW) is a statistical language model used to analyze text and documents based on word count. The model does not account for word order within a document. BoW can be implemented as a Python dictionary with each key set to a word and each value set to the number of times that word appears in a text.

# the sentence "Squealing suitcase squids are not like regular squids." could be changed into the following BoW dictionary:

{'squeal': 1, 'like': 1, 'not': 1, 'suitcase': 1, 'be': 1, 'regular': 1, 'squid': 2}


Feature Extraction in NLP
Feature extraction (or vectorization) in NLP is the process of turning text into a BoW vector, in which features are unique words and feature values are word counts.

# given the following features dictionary mapping:
{'are':0, 
 'many':1, 
 'success':2, 
 'there':3, 
 'to':4, 
 'ways':5}

# "many success ways" could be represented
# as the following BoW vector:
[0, 1, 1, 0, 0, 1]


Bag-of-words Test Data
Bag-of-words test data is the new text that is converted to a BoW vector using a trained features dictionary. The new test data can be converted to a BoW vector based on the index mapping of the trained features dictionary.

For example, given the training data “There are many ways to success.” and the test data “many success ways”, the trained features dictionary and the test data BoW vector could be the following.

# the trained features dictionary
{'are':0, 
 'many':1, 
 'success':2, 
 'there':3, 
 'to':4, 
 'ways':5}

# the test data BoW vector
[0, 1, 1, 0, 0, 1]


Feature Vector
In machine learning, a feature vector is a numeric depiction of an object’s salient features. In the case of bag-of-words (BoW), the objects are text samples and those features are word counts.

For example, given this features dictionary mapping, a BoW feature vector of “Another five fish find another faraway fish.” would be [1, 0, 2, 0, 0, 0, 1, 1, 0, 0, 2].

{'five': 0,
'fantastic': 1,
'fish': 2,
'fly': 3,
'off': 4,
'to': 5,
'find': 6,
'faraway': 7,
'function': 8,
'maybe': 9,
'another': 10}


Language Smoothing in NLP
Language smoothing is a solution to avoid overfitting in NLP. It takes a bit of probability from known words and allots it to unknown words. This causes the unknown words to have a probability of more than 0.

Features Dictionary in NLP
A features dictionary is a mapping of each unique word in the training data to a unique index. This is used to build out bag-of-words vectors.

For instance, given the training data “Squealing suitcase squids are not like regular squids”, the features dictionary could be as the following.

{'squeal': 0, 'suitcase': 1, 'squid': 2, 'be': 3, 'not': 4, 'like': 5, 'regular': 6}


Bag-of-words Data Sparcity
Bag-of-words has less data sparsity (i.e., it has more training knowledge to draw from) than other statistical models. When vectorizing a document, the vector is considered sparse if the majority of its values are zero which means that most of the words are not contained in the vocabulary design. BoW also suffers less from overfitting (adapting a model too strongly to training data).

Perplexity in NLP
For text prediction tasks, the ideal language model is one that can predict an unseen test text (gives the highest probability). In this case, the model is said to have lower perplexity.

Bag-of-words has higher perplexity (it is less predictive of natural language) than other models. For instance, using a Markov chain for text prediction with bag-of-words, you might get a resulting nonsensical sequence like: “we i there your your”.

A trigram model, meanwhile, might generate the far more coherent (though still strange): “i ascribe to his dreams to love beauty”.
