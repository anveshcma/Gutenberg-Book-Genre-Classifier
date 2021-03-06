import sys,os
sys.path.append( os.path.join(".."))
from UtilityFunctions import CommonHelpers, PreprocessHelpers, FeatureEngineering
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD

class BoW_Vectors:
    def __init__(self):
        self.PREPROCESSED_STORE_LOC = os.path.join("..","data","preprocessed")


    def load_data(self):
        self.all_books = CommonHelpers.load_pickle(os.path.join(self.PREPROCESSED_STORE_LOC,"books_english_preprocessed.pickle"))
        self.combined_books = [' '.join(book) for book in self.all_books]
        

    def create_vectors(self):
        self.vectorizer = CountVectorizer( analyzer='word', token_pattern=r'\w{1,}')
        self.bow_vectors = self.vectorizer.fit_transform(self.combined_books)


    def dim_reduce_svd(self):
        self.svd = TruncatedSVD(n_components=300, n_iter=7, random_state=42)
        self.svd_bow_vectors = self.svd.fit_transform(self.bow_vectors)


    def dim_reduce_pca(self):
         self.pca = PCA(n_components=300)
         self.pca_bow_vectors = self.pca.fit_transform(self.bow_vectors)


    def save_pickles(self, type='full'):
        if type == 'SVD':
            CommonHelpers.dump_pickle("../data/feature/svd_bow_vectors.pickle",self.svd_bow_vectors)        
        else:
            CommonHelpers.dump_pickle("../data/feature/bow_vectors.pickle",self.bow_vectors)


    def load_pickles(self, type='full'):
        if type == 'SVD':
            self.book_vectors = CommonHelpers.load_pickle("../data/feature/svd_bow_vectors.pickle")
        else:
            self.book_vectors = CommonHelpers.load_pickle("../data/feature/bow_vectors.pickle")

 