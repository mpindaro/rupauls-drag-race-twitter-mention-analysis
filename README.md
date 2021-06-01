# RuPaul's Drag Race Season 13 Twitter Mentions Analysis

```Margherita Pindaro, 923178, progetto per il corso di Social Media Mining AA 2021-21.```

Analisi del grafo delle menzioni su Twitter riguardanti la tredicesima edizione di *RuPaul's Drag Race*.

[📌 Slides](https://docs.google.com/presentation/d/1sN9N81PgTzeoIlaSFHMxxlrrNCHMJ30KPHdwpAidLwU/edit?usp=sharing&resourcekey=0-vRqR4GDD3iwIfREx0eM7MQ)

> RuPaul's Drag Race è un reality show statunitense che si basa su una competizione tra drag queen. Ogni settimana i concorrenti vengono giudicati per le loro performance da vari giudici e al termine di ogni episodio vengono scelti i concorrenti top e due concorrenti bottom  i quali affrontano una prova finale chiamata lipsync che determina l’eliminazione.
> Inoltre, in ogni edizione, oltre all'elezione dell'America's Next Drag Superstar, viene anche eletta Miss Simpatia (Miss Congeniality).

Il progetto comprende:
- Analisi delle **proprietà fondamentali** di una rete.
- **Review su diversi indici di centralità** in base al ranking da loro prodotti e la similarità (Kendall Tau e Hamming) con il ranking reale della stagione.
- Analisi dell'**andamento di ciascun concorrente** settimana per settimana nelle discussioni su Twitter.
- Verifica che durante il *lipsync*, la prova finale ad eliminazine, **i due concorrenti con più menzioni siano effettivamente quelli che stanno svolgendo la suddetta prova**.
- S**entiment Analysis sui tweet** che menzionano un concorrente, stimando così per ogni concorrente uno score di *likeability*.
- **Identificazione di community di utenti outliers** tramite user clustering.

⚠️I tweet raccolti **non** sono presenti nella repo per motivi di privacy⚠️

📒 Notebook raccolta dati:
- [Raccolta tweet tramite Twitter Streaming API](RuStreaming.ipynb)
- [Scraping delle informazioni dei concorrenti](ScrapWikiDrag.ipynb)
- [Raccolta di termini slang del contesto](ScrapDragTerms.ipynb)

📒 Notebook analisi:
- [Analisi del Network](NetworkAnalysis.ipynb)
- [Analisi dei singoli episodi](SingleEpisodeAnalysis.ipynb)
- [Sentiment Analysis](SentimentAnalysis.ipynb)
- [Clustering Based Outlier Detection](ClusteringBasedOutlierDetection.ipynb)
