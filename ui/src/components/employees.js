import React from 'react'
import { Table, Button, Alert } from 'react-bootstrap';

const Employees = ({ employees }) => {
  return (
    <div width="100%">
      <center><h1>Employee List</h1></center>
      <br/>
      <table width="100%">
      <thead>
      <tr>
      <th width="20%">Code</th>
      <th width="20%">Name</th>
      <th width="20%">Age</th>
      <th width="20%">Address</th>
      <th width="20%">Department</th>
      <th>Action</th>
      </tr>
      </thead>
      <tbody>
      {employees.map((employee) => (
        <tr>
        <td width="20%">{employee.code}</td>
        <td width="20%">{employee.name}</td>
        <td width="20%">{employee.age}</td>
        <td width="20%">{employee.address}</td>
        <td width="20%">{employee.department}</td>
        <td>
        <Button variant="info" onClick={() => this.props.editProduct(product.id)}>Edit</Button>
        &nbsp;
        <Button variant="danger" onClick={() => this.deleteProduct(product.id)}>Delete</Button>
        </td>
        </tr>

      ))}
      </tbody>
      </table>
    </div>
  )
};

export default Employees
