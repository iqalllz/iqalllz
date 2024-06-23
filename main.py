import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import token_recognizer
import validation
import stack

SUBJECT = ["nana", "nini", "nunu", "nene", "nono"]
PREDICATE = [
    "memiliki",
    "mempunyai",
    "menjadi",
    "mengerjakan",
    "membangun",
]
OBJECT = [
    "sekolah",
    "rumah",
    "guru",
    "tugas",
    "masjid",
]
KETERANGAN = [
    "di maluku",
    "di papua",
    "di jawa",
    "di madura",
    "di togo",
]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Home",
                    children=[
                        html.H1("Welcome to the Token Recognition App"),
                        html.P(
                            "This app allows you to tokenize and validate sentences based on predefined rules."
                        ),
                    ],
                ),
                dcc.Tab(
                    label="Token Recognition",
                    children=[
                        html.H1("Token Recognition and Sentence Validation"),
                        dcc.Input(
                            id="sentence-input",
                            type="text",
                            placeholder="Enter sentence",
                            debounce=True,
                            style={
                                "width": "50%",  # Adjust the width as desired (e.g., "100%")
                                "resize": "both",  # Allow resizing horizontally and vertically
                                "overflow": "auto",
                            },
                        ),
                        html.Div(id="token-output"),
                        html.Div(id="validation-output"),
                        html.H2("Dictionary"),
                        html.H3("Subject"),
                        html.Ul([html.Li(word) for word in SUBJECT]),
                        html.H3("Predicate"),
                        html.Ul([html.Li(word) for word in PREDICATE]),
                        html.H3("Object"),
                        html.Ul([html.Li(word) for word in OBJECT]),
                        html.H3("Keterangan"),
                        html.Ul([html.Li(word) for word in KETERANGAN]),
                    ],
                ),
                dcc.Tab(
                    label="About Us",
                    children=[
                        html.H1("About Us"),
                        html.P(
                            """
            This application was created to demonstrate the use of token recognition and sentence validation using a Finite Automata and Push Down.
            It allows users to input sentences and check their validity based on specific grammatical rules.
            """
                        ),
                        html.P("Developed by:"),
                        html.P("- Adrian Prakoso Harianto (1301220278)"),
                        html.P("- Muhammad Iqbal Rizaldy (1301220343)"),
                        html.P("- Iqal Mahendra Laksono (1301223243)"),
                    ],
                ),
            ]
        )
    ]
)


@app.callback(
    [Output("token-output", "children"), Output("validation-output", "children")],
    [Input("sentence-input", "value")],
)
def update_output(sentence):
    if sentence:
        s = stack.Stack()
        tr = token_recognizer.TokenRecognizer()
        v = validation.Validation(s)

        token = tr.set_token(sentence=sentence)
        is_valid = v.validate(tokens=token)

        token_output = f"Tokens: {token}"
        validation_output = (
            f"'{sentence}' is valid" if is_valid else f"'{sentence}' is not valid"
        )

        return token_output, validation_output
    return "", ""


if __name__ == "__main__":
    app.run_server(debug=True)
