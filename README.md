# Toy
Short-term Toy Project


## AB TEST
[Document](https://www.notion.so/A-B-Test-5b6bfcf642eb4b92bd7d4328cb321959)

## World of Warcraft Raid Purchaser Count
The World of Warcraft Korean Realms raid parties are mostly goal parties. Dungeon, which has a low distribution amount, is a structure in which players cannot receive gold when they acquire items, and it is a project that is carried out to classify them easily. this project based on Python tkinter library. It will be updated periodically.

## Categorical Feature Encoding
[Data Source](https://www.kaggle.com/c/cat-in-the-dat/data)  
[Reference Kernel](https://www.kaggle.com/shahules/an-overview-of-encoding-techniques)

A common task in machine learning pipelines is encoding categorical variables for a given algorithm in a format that allows as much useful signal as possible to be captured.

Because this is such a common task and important skill to master, we've put together a dataset that contains only categorical features, and includes:
- binary features
- low- and high-cardinality nominal features
- low- and high-cardinality ordinal features
- (potentially) cyclical features

### Label Encoder
This method change every categorical data to number. For example we substitute 1 for cat, 2 for dog, 3 for tiger...

### One Hot Encoding
One Hot Encoding, in the same way as dummy coding, is a method of creating and reconstructing variables that take 1 or 0 according to the number of categories.

![](https://miro.medium.com/max/1200/0*T5jaa2othYfXZX9W.)

### Feature Hashing
Feature Hashing is similar to One Hot Encoding, but it has the advantage of being able to determine dimensions.

### Statistics Encoding
Statistical method using frequency. Assume that similar frequencies by category are similar. If the frequency of Seoul and Incheon are similar, it is a similar category.

### Cyclic Encoding
![](https://miro.medium.com/max/343/1*70cevmU8wNggGJEdLam1lw.png)

Some of our features are cyclic in nature.ie day,month etc.

A common method for encoding cyclical data is to transform the data into two dimensions using a sine and consine transformation.

### Using Model
- Logistic Regrssion
    - Hyper Parameter
        - C = 0.1

### Result
<img src="https://github.com/SSANGMAN/Toy/blob/master/Categorical%20Feature%20Encoding/asset/comparision.png?raw=true" width = "400">
