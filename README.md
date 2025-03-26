# Homework 3 - Unsupervised Learning and Writing a Data Science Report
Authors: Dylan Cashman and Binyamin Friedman

## Background

A recent article in [Harvard Business Review](https://hbr.org/2019/01/data-science-and-the-art-of-persuasion) highlighted that the communication of data science conclusions is one of the biggest hurdles in getting the most out of our data.  According to a 2017 Kaggle interview of data scientists, 

> four of the top seven “barriers faced at work” were related to last-mile issues, not technical ones: “lack of management/financial support,” “lack of clear questions to answer,” “results not used by decision makers,” and “**explaining data science to others**.”

Machine learning is an exciting field because it is able to do things with data that we never thought possible before: interpret images, video, text, improve weather forecasting, achieve superhuman levels of machine translation, and a number of other exciting examples.  However, we tend to only hear about the successes, which are often the end result of dozens of years of dataset gathering, cleaning, trials and errors, and iterations within collaborative teams of data scientists, machine learning engineers, and subject matter experts.

## Overview
In this programming assignment, you will gain experience working as a data scientist (and using unsupervised machine learning methods) and then presenting your results to a layperson. 

You've been having a great time at your Quant internship, analyzing nicely documented datasets from the firm's primary data store. After lunch one day, your boss tells you that while cleaning out her file cabinet (she explains how this is the other intern's job), she found an intriguing dataset of portfolio gains and losses. The catch? She just cannot remember what any of the columns refer to... She wants you to,
1. Use data visualization and unsupervised machine learning to make sense of the dataset
2. Put together a slideshow presentation and record a 5-minute presentation describing your conclusions

### Notes
- The main dataset, [data/portfolio.csv](data/portfolio.csv), contains 25k rows and 26 columns: a date field and 25 numerical values representing financial portfolio gains and losses. 
- An additional file, [data/recessions.csv](data/recessions.csv), contains additional information on whether a given month was considered a recession or not. **You do not have to use this file**, although you may be interested in seeing this recession data and you are allowed to use it in your analysis if you'd like. 
- As with PA2, we expect you to load the data into a Jupyter notebook to complete most of the tasks in this assignment. Then, we want you to copy over your code into the provided python package skeleton.  

## Grade Breakdown

### Notebook (70 points)
Follow the instructions in [exploration.ipynb](notebooks/exploration.ipynb)
### Python Deliverable (10 points)
Now, you need to make a decision about which results you want to go into your report. First, pick a particular clustering method and a particular projection method. 

In the provided python package skeleton,
- Your code that generates the projections should go in `projections.py`  
- Your code that generates the clusters in `clusters.py` 
- And your code that generates the charts into `visualizations.py`, using the `savefig` method to save your charts to .png files.  

The expected structure would be that your `visualizations.py` file would include function(s) from `projections.py` and `clusters.py`, and would run those methods and then generate figures.  There is some skeleton code that shows methods being imported into that file that you can start from.

You should be able to run `python src/visualizations.py` from the `PA3_unsupervised_learning` folder, and it should generate new figures in the `figures/` folder.  

### Presentation (20 points)
Create a 5-minute slideshow presentation of your results on the dataset. Your goal is to tell a cohesive summary, a narrative with a key takeaway (or multiple). It should include the following: 
- A summary of the dataset, with any interesting observations you've made. Here, you should show your line chart and pick out particular histograms that you find interesting (please do not just show 26 tiny plots).
- A brief explanation of the clustering method that you used: no diagrams are necessary, but you should explain what the different clusters mean in a way that an economist might understand. You can show your cluster centroid/core-sample table.
- A brief explanation of the projection method that you used. You should show your projection with the points colored by what cluster they appear in.
- Some conclusion based on the previous analysis.

Some notes about slideshow design,
- The most important thing for a slideshow is that the listener can easily grasp the main point of any slide
- The slideshow functions as an aid to following the speaker, it is not a document to be read carefully 
- Try to not be too verbose
- Make sure the slides are visually appealing and easy to read, with a consistent theme (this is not the same as fancy animations or graphics, simple is often better)

We have included a skeleton powerpoint presentation with the sections that we expect.  Please feel free to use your own styling as long as it includes those sections.  You are also free to use any other slides software (i.e. keynote, Google slides, etc.) as long as you share the slides with us.

Along with the slideshow presentation, you must record yourself going through your slides, as if you were presenting to an audience. Your goal is to sound knowledgeable and confident about your conclusions (even if your conclusion is admitting some issue). This should be quick, between 4 and 6 minutes. You can use any method you are comfortable with.  

You may use the [built-in screen recorder from Powerpoint](https://support.microsoft.com/en-us/office/record-a-presentation-2570dff5-f81c-40bc-b404-e04e95ffab33) or you may use [Zoom to record your screen](https://harrell.library.psu.edu/c.php?g=1012321&p=7384247).

Upload your slides and video to the [Brandeis Google drive](drive.google.com), change the share permissions of the file so that anyone with a brandeis.edu email address can view it. 

Lastly, link your slideshow and video in [presentation/README.md](presentation/README.md).