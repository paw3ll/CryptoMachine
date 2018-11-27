# CryptoMachine
A work in progress project for learning Python and Machine learning. Utilizing API from various concurrency markets.  

Project Motivation:
What are the reasons for doing the project?
* To study and explore the principle of relaxation, in shortest-path algorithms (i.e Dijkstra, Bellman-Ford, Johnson, Floyd-Warshall)  whereby costs are initially overestimatedfor all vertices and gradually corrected for using a consistent heuristic on edges.
* To study and explore the principle of relaxation using reinforcement learning in currency arbitrage: to effectively detect negative cycles in graphs representing currency markets
    * Cryptocurrency Market because data is public, free, and easy to obtain.
     * Utilizing streaming APIs that allow you to receive market updates in real-time.
     * GDAX / Coinbase API. https://docs.gdax.com
What do you benefit of the proposed project?
  * Shortest Path algorithms are an essential part of a computer science / engineering curriculum and relatively “easy” to implement (particularly Bellman-Ford)
  * The topics covered -finance, shortest paths algorithms, reinforcement learning -provide us with an opportunity to use Python to implement the ideas using probability theory and calculus,  essential for data science and data analysis.
  * Shortest path algorithms used in conjunction with understanding of cryptocurrency market / foreign exchange market can potentially offer monetary gains → efficiently detecting negative cycles in graphs is a multi-billion dollar business.
  
 Project Description:Objective of proposed project
  * Increase understanding of shortest path algorithms, finance markets, abstract theory, calculus, python and application creation. 
 * Project Explanation:
   * Data Source. 
    * API from selected market: Cryptocurrency. GDAX / Coinbase
   * How will you extract the data?
    * The data required must be scraped from the API of the selected market of the selected site. This will prevent us from having to manually input the data / track it real time. 
   * How will you pre-process the data?
    * While the exact methods for pre-processing are TBH we anticipate that we may be required to rescale in the case of needing crisp values the data may need to be baniarized, and finally the data will have to be standardized to transform attributes with a Gaussian distribution and differing means and standard deviations to a standard Gaussian distribution with a mean of 0 and a standard deviation of 1.
   * How will you archive the data?
    * SQL Database / Excel Spreadsheet. 
   * How will you process the data?
    * Exploring Soft-Q learning, PGQ/PCL, and Distributional Reinforcement Learning which are "probabilistically aware'' reinforcement learning algorithms.
    * Standard Machine Learning practices such as: Cross Validation which will be required for training of the algorithm.○How will you visualize the data?
    * We will be utilizing Python data visualization methods such as  Nupy, Scikitlearn, Pandas, and matplot lib (https://blog.modeanalytics.com/python-data-visualization-libraries/)
    * The exact libraries for visualization to be implemented as needed. 

