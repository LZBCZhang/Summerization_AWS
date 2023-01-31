import React from 'react';
import ReactDOM from 'react-dom';

class TextArea extends React.Component {
    constructor(props) {
        super(props);
        this.state = { text: '' };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.setState({ text: e.target.value });
    }

    render() {
        return (
            <div>
                <textarea
                onChange = { this.handleChange }
                defaultValue = { this.state.value }
                />
            </div>
        );
    }
}

ReactDOM.render(
    <TextArea />,
    document.getElementById('root')
);