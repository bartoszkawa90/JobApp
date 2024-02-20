import React, { Component } from "react";

class Header extends Component{
    render() {
        return (
            <div>
                <img
                    src="https://looka.com/editor/172565811"
                    width="500"
                    className="img-thumbnail"
                    style={{ marginTop: "20px"}}
                />
                <hr />
                <h1> Jobs Offers from some popular websites </h1>
            </div>
        );
    }
}

export default Header;