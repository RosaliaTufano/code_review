import opennmt


class MyCustomTransformer(opennmt.models.Transformer):
    def __init__(self):
        super().__init__(
            source_inputter=opennmt.inputters.WordEmbedder(256),
            target_inputter=opennmt.inputters.WordEmbedder(256),
            num_layers=[1, 2],
            num_units=256,
            num_heads=8,
            ffn_inner_dim=512,
            dropout=0.319,
            attention_dropout=0.3985,
            ffn_dropout=0.0998)


model = MyCustomTransformer
