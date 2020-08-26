import opennmt


class MyCustomTransformer(opennmt.models.Transformer):
    def __init__(self):
        super().__init__(
            source_inputter=opennmt.inputters.ParallelInputter(
                [opennmt.inputters.WordEmbedder(embedding_size=2048),
                 opennmt.inputters.WordEmbedder(embedding_size=2048)]),
            target_inputter=opennmt.inputters.WordEmbedder(embedding_size=2048),
            num_layers=[4, 3],
            num_units=2048,
            num_heads=8,
            ffn_inner_dim=256,
            dropout=0.0341,
            attention_dropout=0.2114,
            ffn_dropout=0.0735,
            share_encoders=True)


model = MyCustomTransformer
