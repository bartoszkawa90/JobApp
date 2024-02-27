import React, { Component } from "react";
import {Col, Container, Row, Table} from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
    state = {
        offers: []
    };

    render() {
        return (
            <Table dark>
                <thead>
                    <tr>
                        <th> Title </th>
                        <th> Responsibilities </th>
                        <th> Requirements </th>
                        <th> Link </th>
                    </tr>
                </thead>
                <tbody>
                    {!students || students.length <= 0 ? (
                        <tr>
                          <td colSpan="6" align="center">
                            <b>Ops, no one here yet</b>
                          </td>
                        </tr> ):
                </tbody>
            </Table>

        )
    }
}
