
import React from 'react';
import { Table, Button, Alert } from 'react-bootstrap';

class ProductList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      products: [],
      response: {}
    }
  }

  componentDidMount() {
    const apiUrl = 'http://127.0.0.1:8000/employees/';

    fetch(apiUrl)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            products: result
          });
        },
        (error) => {
          this.setState({ error });
        }
      )
  }

  deleteProduct(code) {
    const { products } = this.state;

    const apiUrl = 'http://127.0.0.1:8000/employees/delete/' + code;
    const formData = new FormData();
    formData.append('code', code);

    const options = {
      method: 'GET'//,
      //body: formData
    }

    fetch(apiUrl, options)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            response: result,
            products: products.filter(product => product.code !== code)
          });
        },
        (error) => {
          this.setState({ error });
        }
      )
  }

  render() {
    const { error, products} = this.state;

    if(error) {
      return (
        <div>Error: {error.message}</div>
      )
    } else {
      return(
        <div>
          <h2>Employee List</h2>
          {this.state.response.code && <Alert variant="info">Employee(CODE: {this.state.response.code}) deleted successfully!</Alert>}
          <Table>
            <thead>
              <tr>
                <th>#Code</th>
                <th>Name</th>
                <th>Age</th>
                <th>Address</th>
                <th>Department</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {products.map(product => (
                <tr key={product.code}>
                  <td>{product.code}</td>
                  <td>{product.name}</td>
                  <td>{product.age}</td>
                  <td>{product.address}</td>
                  <td>{product.department}</td>
                  <td>
                    <Button variant="info" onClick={() => this.props.editProduct(product.code)}>Edit</Button>
                    &nbsp;<Button variant="danger" onClick={() => this.deleteProduct(product.code)}>Delete</Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        </div>
      )
    }
  }
}

export default ProductList;
