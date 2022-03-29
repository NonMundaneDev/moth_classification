
# 1. Problem Statement
### What is the overall project concept from the client?

The overall concept of the project is to build an app that is powered by machine learning at the backend. The machine learning software should be able to classify video streams from a raspberry pi computer which is meant to sense motion of insects in the farm, capture ths stream, and pass it to a machine learning software for inference. Once the software classifies the type of moth based on their species tags/labels, sends this classification (and other metadata like time, date, and probability of being the true label) to a cloud system which through some Cloud service triggers gets the image and metadata of the classified species and sends it through an API to a phone application that uses that information for visual communication of key, domain-specific ideas to the user.


### What is the problem we are trying to solve?
We are trying to save farmers and farm stakeholders a lot of money by helping them build an automated system that can notify them of the presence of 1 or 3 specific species of moths in the farm through detection and automatic classification of the species in the farm.


### Is this a machine learning problem?
To understand if a problem is a machine learning problem, we need to understand the following (I also add the answers below);

**Question 1:** Is this problem already performed by humans? If yes, how?

**Answer:** Yes, farmers already use their eyes to detect, count, and classify what type of moth species has invaded the farm and the use insecticide to elimnate these pests. This is a very repetitive and tedious process for them.

**Analysis 1:** 
- Based on the question and answer, this problem seems to be worthy of being classed as a machine learning use-case because it is repetitive and challenging but not impossible for humans to do.

- The problem is also specific enough because it is all about classifying the type of moth species (of 3 different labels) in an image or footage.


**Question 2:** Can the data for the problem be gotten? If yes, how does the data come in and how easy is it to get the data?

**Answer:** Yes, the data can be gotten. Altough the pests come in seasonally based on the plant season for the maize crop; if it is still in its budding stage.


**Analysis 2:** 

- Based on our conversation with the entomologist, the moth species migrate to the farm only at specific times during the farming season and the species availability is also dependent on the growth of the maize plant. If the plant is still at its budding stage, it would most likelt attract the moth as it would be easy for them to breed on the plants.

- Judging from our discussion with the entomologist as well, since we are trying to automate the identification of the pest, it would be worthwhile identifying the male species of the pest rather than both species because it is pretty much the initiator of the crop damage through mating and breeding.


**Question 3:** Are there many features for the data? 

**Answer:** The data is an image data hence there is a high dimension of features available in the image data.

**Analysis 3:** 

- The distinguishing feature between each of the labels are not very evident but I think this is a problem ripe for a deep learning algorithm rather than traditionally hand-crafting the features for an algorithm to understand.



---

### Proposed Architecture for the Project



![AI MAIZE PEST Architecture (1).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1598007863071/gy8cj-M6t.png)

---

# 2. Getting Data Relevant to the Problem

### Here are some concerns for us when trying to get data relevant to this problem:

**Question:** What type of data is needed for this project and how much data is needed for the project?

**Answer:** The type of data needed for this project are image data sets of each of the various species.

**Question:** What are the typical challenges we face whenever we want to get data like this?

**Answer:**

1. Avaialbility of a human (domain) expertise to help us classify what photos or footages of moth contain what species.

2. Getting a real-time footage or image capture of moth species in the production envrionment (the farm) is a challenging process. To lure the moth into the farm, we had to use what is called a Pheromone trap as recommended by the entomologist working with us on this project.

---




