
# Python Module Documentation

## Functions

### 1. mean(data)
- **Description**: Returns the mean of the list data.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The mean value of the list, rounded to two decimal places.

### 2. setOutlier(data, low, high)
- **Description**: Removes outliers outside the set low and high values.
- **Arguments**: 
  - `data` - a list of numeric values.
  - `low` - the lower bound value.
  - `high` - the upper bound value.
- **Returns**: A list with outliers removed.

### 3. imputate(data, low, high)
- **Description**: Replaces invalid values in the data (outside low and high) with the mean of the filtered data.
- **Arguments**:
  - `data` - a list of numeric values.
  - `low` - the lower bound value.
  - `high` - the upper bound value.
- **Returns**: A list with invalid values replaced by the mean.

### 4. median(data)
- **Description**: Returns the median of the list data.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The median value of the list.

### 5. mode(data)
- **Description**: Returns the mode (most frequent value) of the list data.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The mode value, or None if all values are unique.

### 6. freq(data, value)
- **Description**: Returns the frequency (count) of a specific value in the list data.
- **Arguments**:
  - `data` - a list of values.
  - `value` - the value to count.
- **Returns**: The count of occurrences of the value in the list.

### 7. gen(length, low, high, type)
- **Description**: Generates a list of random values of the specified type and length.
- **Arguments**:
  - `length` - the length of the list to generate.
  - `low` - the lower bound for numeric values (ignored for non-numeric types).
  - `high` - the upper bound for numeric values (ignored for non-numeric types).
  - `type` - the type of values to generate (options: 'number', 'animal', 'name', 'fruit', 'vegetable', 'county', 'country').
- **Returns**: A list of randomly generated values.

### 8. Range(data)
- **Description**: Returns the range (difference between the max and min) of the list.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The range of the list.

### 9. replace(data, old, new)
- **Description**: Replaces every occurrence of `old` value in the list with the `new` value.
- **Arguments**:
  - `data` - a list of values.
  - `old` - the value to be replaced.
  - `new` - the new value to replace with.
- **Returns**: The modified list with replaced values.

### 10. stdDev(data)
- **Description**: Returns the standard deviation of the list.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The standard deviation of the list, rounded to two decimal places.

### 11. variance(data)
- **Description**: Returns the variance of the list.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The variance of the list, rounded to two decimal places.

### 12. iqr(data)
- **Description**: Returns the Interquartile Range (IQR) of the list.
- **Arguments**: `data` - a list of numeric values.
- **Returns**: The IQR of the list, rounded to two decimal places.

### 13. zScore(data, value)
- **Description**: Returns the z-score of a specific value in the list, using the list as a dataset.
- **Arguments**:
  - `data` - a list of numeric values.
  - `value` - the value to calculate the z-score for.
- **Returns**: The z-score of the value.

### 14. percentile(z_score)
- **Description**: Returns the percentile corresponding to a given z-score.
- **Arguments**: `z_score` - the z-score value.
- **Returns**: The percentile value, rounded to two decimal places.

### 15. outlier(data, z_ScoreCutoff=2)
- **Description**: Automatically removes outliers in the data outside a set z-score cutoff.
- **Arguments**:
  - `data` - a list of numeric values.
  - `z_ScoreCutoff` - the cutoff z-score for defining outliers (default: 2).
- **Returns**: The list with outliers removed.

### 16. merge(list1, list2)
- **Description**: Merges two lists into a list of tuples.
- **Arguments**:
  - `list1` - the first list.
  - `list2` - the second list.
- **Returns**: A list of tuples, where each tuple contains corresponding elements from both lists.

### 17. covariance(list1, list2)
- **Description**: Returns the covariance of two lists.
- **Arguments**:
  - `list1` - the first list of numeric values.
  - `list2` - the second list of numeric values.
- **Returns**: The covariance between the two lists, rounded to two decimal places.

### 18. correlate(list1, list2)
- **Description**: Returns the correlation coefficient between two lists.
- **Arguments**:
  - `list1` - the first list of numeric values.
  - `list2` - the second list of numeric values.
- **Returns**: The correlation coefficient, rounded to two decimal places.

### 19. slope(list1, list2)
- **Description**: Calculates the slope of a linear regression line between two lists.
- **Arguments**:
  - `list1` - the first list of numeric values.
  - `list2` - the second list of numeric values.
- **Returns**: The slope of the linear regression line, rounded to two decimal places.

### 20. regression(list1, list2, value)
- **Description**: Calculates the regression line value for a given input using two lists.
- **Arguments**:
  - `list1` - the independent variable list (X).
  - `list2` - the dependent variable list (Y).
  - `value` - the X-value for which to predict Y.
- **Returns**: The predicted Y-value for the input X-value.

### 21. all(*args)
- **Description**: Returns a comprehensive statistical analysis for all provided lists and compares multiple lists.
- **Arguments**: Multiple lists of numeric values.
- **Returns**: Various statistical measures, including mean, median, mode, standard deviation, variance, range, and more.

### 22. help()
- **Description**: Prints a summary of all available functions and their usage.

