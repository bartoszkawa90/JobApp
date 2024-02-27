import React, { Component } from "react";
import logo from './logoHD.png'


class Header extends Component{
    headerStyle = {
        backgroundColor: '#333', // Replace with your preferred color code
        color: '#fff', // This sets the text color to white
        padding: '10px',
        textAlign: 'left'
    };

    availableWidth = window.screen.availWidth;
    availableHeight = window.screen.availHeight;
    render() {
        return (
            <header style={this.headerStyle}>
                <div style={{alignItems: "center"}}>
                    <div className="image-container">
                        <img src={logo} alt="logo" alt="Round Image" width={this.availableWidth / 5} height={this.availableHeight / 6}
                             style={{margin: "20px", marginTop: "0px", borderRadius: '50%'}}/>
                        <h1 style={{margin: "20px", marginTop: "20px"}}> Jobs Offers from some popular websites </h1>
                        <hr/>
                    </div>
                </div>
            </header>
        );
    }
}

export default Header;