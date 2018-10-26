# Analysis-of-potential-topics-based-on-GitHub-source-code
Graduation Project in Beihang University

This project was implemented between 10/2017 to 06/2018.

Code topic analysis is an important part of software reuse and software rewriting. Developers need to first analyze the basic themes of the code to make better use of the code before adding software features, modifying software defects, and reusing software code. Code latent topic analysis can be implemented either through the code itself or through related documents and texts, such as requirements analysis documents, related comments, and so on. Although these related documents are relatively easy to understand, their susceptibility to loss makes code projects often difficult to understand and cannot be used more. Of course, in recent years, with the popularity of agile development methods, many softwares no longer have independent documents, and the code is a document. Therefore, the subject of the project can also be intuitively understood through the code.

 This project will comprehensively analyze code and related documents and analyze the effect of topic extraction one by one. Through a large number of source project data crawled on the GitHub website, it is effectively pre-processed, and then the subject keyword is effectively extracted through the LDA topic model, and finally the evaluation criteria of the topic extraction result are constructed.The first part includes the collection and processing of data. Data collection is combined with own acquisition and laboratory acquisition. Data processing includes word segmentation, stop words, stemming and other operations.The second part includes the construction and adjustment of the model. By calling sklearn's LDA theme model, the topic extraction of the code is completed, and the optimal theme keyword is obtained by multiple participation in different data set running models. Finally, the effect is evaluated by combining internal methods with self-labeling.
