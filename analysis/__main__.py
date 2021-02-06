from . import analysis
import sys

if __name__ == "__main__" and len(sys.argv) > 1:
  if (sys.argv[1] == "kmeans"):
    analysis.kmeans_analysis()
  elif sys.argv[1] == "pca":
    analysis.pca_analysis()