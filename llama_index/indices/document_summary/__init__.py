"""Document summary index."""


from llama_index.indices.document_summary.base import (
    DocumentSummaryIndex,
    GPTDocumentSummaryIndex,
)
from llama_index.indices.document_summary.retrievers import (
    DocumentSummaryIndexEmbeddingRetriever,
    DocumentSummaryIndexRetriever,
)

__all__ = [
    "DocumentSummaryIndex",
    "DocumentSummaryIndexRetriever",
    "DocumentSummaryIndexEmbeddingRetriever",
    # legacy
    "GPTDocumentSummaryIndex",
]
